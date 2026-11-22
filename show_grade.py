"""Display your Homework 1 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "d56b041166eda921231948a867742e72"
GRADE_HASH = "708d4dc3cefa5245b2bba49b18461bd65592df101bca92696c10157cb371cbdd"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 1: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
