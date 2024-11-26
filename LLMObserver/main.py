from observers.observers.models.openai import wrap_openai
from openai import OpenAI
from observers.stores.duckdb import DuckDBStore

llm=OpenAI()
store=DuckDBStore()
openai_client=wrap_openai(llm,store=store)

response=openai_client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role":"user","content":"what is 100*7"}]
    )
