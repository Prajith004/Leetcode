class Solution(object):
  def splitWordsBySeparator(self, words, separator):
    """
    :type words: List[str]
    :type separator: str
    :rtype: List[str]
    """
    result = []
    for word in words:
      # Split the word and filter out empty strings
      split_words = [w for w in word.split(separator) if w]
      result.extend(split_words)
    return result
