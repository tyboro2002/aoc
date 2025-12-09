#!/bin/bash

# --- Configuration ---
VENV_NAME="env"

# --- 2. Virtual Environment Creëren ---
echo "✨ Creating virtual environment: $VENV_NAME..."
python3 -m venv "$VENV_NAME"

# --- 3. Virtual Environment Activeren ---
# Dit is nodig om 'pip' in de venv te kunnen gebruiken
source "$VENV_NAME/bin/activate"

# --- 4. Shapely Installeren ---
echo "📦 Installing shapely inside $VENV_NAME..."
pip install shapely

# --- 5. Installatie Controleren ---
echo "✅ Checking installation..."
python -c "import shapely; print(f'Shapely version installed: {shapely.__version__}')"

# --- 6. Deactiveren ---
deactivate

echo "--- Script Voltooid ---"
echo "De virtual environment is aangemaakt in de map: $VENV_NAME"
echo "Om de omgeving te gebruiken, voer uit: source $VENV_NAME/bin/activate"