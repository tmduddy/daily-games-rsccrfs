from app import GAMES, blocks

assert len(blocks("")) == len(GAMES)
assert "catfishing.net" in blocks(" Catfishing ")[0]["text"]["text"]
assert "Don't know" in blocks("nope")[0]["text"]["text"]
print("ok")
