from collections import Counter

nums = "shailendra kumar is a great person and shailendra is a good person"
freq = Counter(nums)
most_common = freq.most_common(2)
print(most_common)
