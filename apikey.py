# @title Insert API key

from openai import OpenAI

api_key = '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' # @param {type:"string"}

client = OpenAI(api_key=api_key)
