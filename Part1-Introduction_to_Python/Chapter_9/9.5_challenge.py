import random

Nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]

Verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]

Adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]

Prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]

Adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

noun1 = random.choice(Nouns)
noun2 = random.choice(Nouns)
noun3 = random.choice(Nouns)

verb1 = random.choice(Verbs)
verb2 = random.choice(Verbs)
verb3 = random.choice(Verbs)

adjective1 = random.choice(Adjectives)
adjective2 = random.choice(Adjectives)
adjective3 = random.choice(Adjectives)

preposition1 = random.choice(Prepositions)
preposition2 = random.choice(Prepositions)

adverb1 = random.choice(Adverbs)

print(f"A {adjective1} {noun1}")

print(f"A {adjective1} {noun1} {verb1} {preposition1} the {adjective2} {noun2} {adverb1}, the \
{noun1} {verb2} the {noun2} {verb3} {preposition2} a {adjective3} {noun3}")


