import pandas as pd
import pickle
import os
import json

def train_model():
    json_file = "api_logs.json"

    # Check if file exists
    if not os.path.exists(json_file):
        print(f"❌ Error: {json_file} does not exist.")
        return

    # Check if file is empty
    if os.stat(json_file).st_size == 0:
        print(f"❌ Error: {json_file} is empty.")
        return

    try:
        # Print raw file content before reading
        with open(json_file, "r", encoding="utf-8") as f:
            content = f.read()
            print("📂 JSON File Content Before Parsing:\n", content)

        # Load JSON to check if it's valid
        with open(json_file, "r", encoding="utf-8") as f:
            json_data = json.load(f)  # Ensure JSON is valid

        # Read into Pandas DataFrame
        df = pd.read_json(json_file)

        # Check if DataFrame is empty
        if df.empty:
            print("❌ Error: No valid data in api_logs.json.")
            return

        # Convert timestamp to datetime
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
        df["hour"] = df["timestamp"].dt.hour
        df["minute"] = df["timestamp"].dt.minute

        # Simple rate limiting model (count requests per IP)
        model = df.groupby("ip").size().to_dict()

        # Save model
        with open("rate_limit_model.pkl", "wb") as f:
            pickle.dump(model, f)

        print("✅ Model training complete. Saved as rate_limit_model.pkl.")

    except json.JSONDecodeError as e:
        print("❌ JSON Decode Error:", e)
    except ValueError as e:
        print("❌ Pandas JSON Error:", e)

train_model()

