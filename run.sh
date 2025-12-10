#!/bin/bash

# --- Configuration ---
VENV_NAME="env"
source "$VENV_NAME/bin/activate"

# Controleer of alle 3 argumenten zijn meegegeven
if [ "$#" -ne 3 ]; then
    echo "Fout: Gebruik 3 argumenten."
    echo "Gebruik: $0 <DAG> <DEEL> <INPUT_LOCATIE>"
    exit 1
fi

# Wijs de argumenten toe aan duidelijke variabelenamen
DAG="$1"
DEEL="$2"
INPUT_LOCATIE="$3"

if [ "$DAG" -eq 1 ]; then
  if [ "$DEEL" -eq 1 ]; then
    PYTHONPATH=$(pwd):$PYTHONPATH python day1/day1_1.py "$INPUT_LOCATIE"
    exit 0
  fi
  if [ "$DEEL" -eq 2 ]; then
    PYTHONPATH=$(pwd):$PYTHONPATH python day1/day1_2.py "$INPUT_LOCATIE"
    exit 0
  fi
fi

if [ "$DAG" -eq 2 ]; then
  if [ "$DEEL" -eq 1 ]; then
    PYTHONPATH=$(pwd):$PYTHONPATH python day2/day2_1.py "$INPUT_LOCATIE"
    exit 0
  fi
  if [ "$DEEL" -eq 2 ]; then
    PYTHONPATH=$(pwd):$PYTHONPATH python day2/day2_2.py "$INPUT_LOCATIE"
    exit 0
  fi
fi

if [ "$DAG" -eq 3 ]; then
  if [ "$DEEL" -eq 1 ]; then
    PYTHONPATH=$(pwd):$PYTHONPATH python day3/day3_1.py "$INPUT_LOCATIE"
    exit 0
  fi
  if [ "$DEEL" -eq 2 ]; then
    PYTHONPATH=$(pwd):$PYTHONPATH python day3/day3_2.py "$INPUT_LOCATIE"
    exit 0
  fi
fi

if [ "$DAG" -eq 4 ]; then
  if [ "$DEEL" -eq 1 ]; then
    PYTHONPATH=$(pwd):$PYTHONPATH python day4/day4_1.py "$INPUT_LOCATIE"
    exit 0
  fi
  if [ "$DEEL" -eq 2 ]; then
    PYTHONPATH=$(pwd):$PYTHONPATH python day4/day4_2.py "$INPUT_LOCATIE"
    exit 0
  fi
fi

if [ "$DAG" -eq 5 ]; then
  if [ "$DEEL" -eq 1 ]; then
    PYTHONPATH=$(pwd):$PYTHONPATH python day5/day5_1.py "$INPUT_LOCATIE"
    exit 0
  fi
  if [ "$DEEL" -eq 2 ]; then
    PYTHONPATH=$(pwd):$PYTHONPATH python day5/day5_2.py "$INPUT_LOCATIE"
    exit 0
  fi
fi

if [ "$DAG" -eq 6 ]; then
  if [ "$DEEL" -eq 1 ]; then
    PYTHONPATH=$(pwd):$PYTHONPATH python day6/day6_1.py "$INPUT_LOCATIE"
    exit 0
  fi
  if [ "$DEEL" -eq 2 ]; then
    PYTHONPATH=$(pwd):$PYTHONPATH python day6/day6_2.py "$INPUT_LOCATIE"
    exit 0
  fi
fi

if [ "$DAG" -eq 7 ]; then
  if [ "$DEEL" -eq 1 ]; then
    PYTHONPATH=$(pwd):$PYTHONPATH python day7/day7_1.py "$INPUT_LOCATIE"
    exit 0
  fi
  if [ "$DEEL" -eq 2 ]; then
    PYTHONPATH=$(pwd):$PYTHONPATH python day7/day7_2.py "$INPUT_LOCATIE"
    exit 0
  fi
fi

if [ "$DAG" -eq 8 ]; then
  if [ "$DEEL" -eq 1 ]; then
    PYTHONPATH=$(pwd):$PYTHONPATH python day8/day8_1.py "$INPUT_LOCATIE"
    exit 0
  fi
  if [ "$DEEL" -eq 2 ]; then
    PYTHONPATH=$(pwd):$PYTHONPATH python day8/day8_2.py "$INPUT_LOCATIE"
    exit 0
  fi
fi

if [ "$DAG" -eq 9 ]; then
  if [ "$DEEL" -eq 1 ]; then
    PYTHONPATH=$(pwd):$PYTHONPATH python day9/day9_1.py "$INPUT_LOCATIE"
    exit 0
  fi
  if [ "$DEEL" -eq 2 ]; then
    PYTHONPATH=$(pwd):$PYTHONPATH python day9/day9_2.py "$INPUT_LOCATIE"
    exit 0
  fi
fi

if [ "$DAG" -eq 10 ]; then
  if [ "$DEEL" -eq 1 ]; then
    PYTHONPATH=$(pwd):$PYTHONPATH python day10/day10_1.py "$INPUT_LOCATIE"
    exit 0
  fi
  if [ "$DEEL" -eq 2 ]; then
    PYTHONPATH=$(pwd):$PYTHONPATH python day10/day10_2.py "$INPUT_LOCATIE"
    exit 0
  fi
fi