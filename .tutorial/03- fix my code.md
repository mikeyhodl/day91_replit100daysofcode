# Fix My Code

👉 Try and fix this code which is *full* of errors.

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

```python
import requests, json

result = requests.get("https://icanhazdadjoke.com/", headers={"accept":"application/json"}) 

joke = result.json()
```
<details> <summary> 👀 Answer </summary>

```python
import requests, json

result = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"}) # Wrong capitalization

joke = result.json()
print(joke["joke"]) # No output
```
</details>