rem pytest -v -m "sanity" --html=./Reports/allreport.html testCases/ --browser chrome
pytest -v -m "sanity or regression" --html=./Reports/allreport.html testCases/ --browser chrome
rem pytest -v -m "sanity and regression" --html=./Reports/allreport.html testCases/ --browser chrome
rem pytest -v -m "regression" --html=./Reports/allreport.html testCases/ --browser chrome