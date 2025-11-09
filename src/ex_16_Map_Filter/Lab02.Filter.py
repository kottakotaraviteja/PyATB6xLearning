test_results=["PASS","FAIL","SKIP","ERROR"]

pass_give=list(filter(lambda x: x == "PASS", test_results))
print(pass_give)