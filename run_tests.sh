#!/bin/bash

# Stop on any error
set -e

echo "🧹 Cleaning old results..."

# Clean previous artifacts
rm -rf screenshots allure-results allure-report

# Recreate fresh folders
mkdir -p screenshots
mkdir -p allure-results

echo "🚀 Running web tests..."
python3 -m pytest --alluredir=allure-results

echo "📊 Generating Allure report..."
allure generate allure-results -o allure-report --clean

# Optional: auto-open report (comment out if running in CI)
# echo "🌐 Launching Allure report in browser..."
# allure open allure-report