
openai_apikey = "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"
import os
import openai as openai
openai.organization = "org-h0DdGnfsc3nA2yfNZo5XZimF"
openai.api_key = os.getenv("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")
openai.Model.list()

# curl https://api.openai.com/v1/chat/completions \ 
#  -H "Authorization: Bearer $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" \
#  -H "Content-Type: application/json" \
#  -d '{
#     "model": "gpt-3.5-turbo",
#     "messages": [{"role": "user", "content": "Say this is a test!"}],
#     "temperature": 0.7
#   }'