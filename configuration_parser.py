import configparser
import json
import os
import sqlite3
from flask import Flask, jsonify

# Function to read and parse the configuration file
def read_config(file_path):
    config = configparser.ConfigParser()

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Configuration file {file_path} not found")
    
    try:
        config.read(file_path)
        config_data = {}

        for section in config.sections():
            config_data[section] = {}
            for key, value in config.items(section):
                config_data[section][key] = value

        return config_data

    except Exception as e:
        raise Exception(f"Error reading configuration file: {e}")

# Function to save data to SQLite database
def save_to_db(data):
    try:
        conn = sqlite3.connect('config_data.db')
        cursor = conn.cursor()
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS Config (
                            section TEXT,
                            key TEXT,
                            value TEXT
                         )''')
        conn.commit()

        for section, key_values in data.items():
            for key, value in key_values.items():
                cursor.execute('INSERT INTO Config (section, key, value) VALUES (?, ?, ?)', 
                               (section, key, value))
        conn.commit()
        print("Data saved to the database successfully!")

    except Exception as e:
        raise Exception(f"Error saving data to database: {e}")

    finally:
        conn.close()

# Function to save the parsed data into a JSON file
def save_as_json(data, output_file):
    try:
        with open(output_file, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data saved to {output_file}")

    except Exception as e:
        raise Exception(f"Error saving data to JSON: {e}")

# Flask app to serve the config data
app = Flask(__name__)

@app.route('/config', methods=['GET'])
def get_config():
    try:
        conn = sqlite3.connect('config_data.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM Config')
        rows = cursor.fetchall()

        result = {}
        for section, key, value in rows:
            if section not in result:
                result[section] = {}
            result[section][key] = value

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": f"Error fetching data: {e}"})

    finally:
        conn.close()

if __name__ == "__main__":
    config_file = "config.ini"

    try:
        data = read_config(config_file)
        save_as_json(data, 'config_data.json')
        save_to_db(data)

# Run the Flask app

        app.run(debug=True, port=5000)

    except Exception as e:
        print(f"Error: {e}")