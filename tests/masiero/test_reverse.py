import sys 
sys.path.append("packages/masiero/reverse")
import reverse

def test_reverse():
    res = reverse.reverse({"input": "CIAO"})
    assert res["output"] == "OAIC"
