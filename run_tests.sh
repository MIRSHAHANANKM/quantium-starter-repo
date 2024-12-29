touch run_tests.sh
chmod +x run_tests.sh
#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Check if virtual environment activation was successful
if [ $? -ne 0 ]; then
  echo "Error: Failed to activate virtual environment."
  exit 1
fi

# Install dependencies
pip install -r requirements.txt
if [ $? -ne 0 ]; then
  echo "Error: Failed to install dependencies."
  deactivate
  exit 1
fi

# Run the test suite
pytest test_app.py
if [ $? -eq 0 ]; then
  echo "All tests passed successfully."
  deactivate
  exit 0
else
  echo "Some tests failed. Please check the output above."
  deactivate
  exit 1
fi
