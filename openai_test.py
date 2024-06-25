from openai import OpenAI

client = OpenAI()

def generate_blog_post(messages, model="gpt-4o", max_tokens=1000, temperature=0.7, top_p=1.0, n=1):
    try:
        # OpenAI API를 사용하여 텍스트 생성 요청
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            n=n
        )

        # 생성된 텍스트 반환
        print(response)
        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"Error: {e}")
        return None

messages = [
    {"role": "user", "content": "백엔드 기술 중 하나에 대해 글을 써줘 퀄리티는 2년차 개발자가 쓴 것 처럼"},
    {"role": "user", "content": "블로그에 올릴 수 있을 정도로 사람이 쓴 것 처럼"},
    {"role": "user", "content": "소개 글 빼고 마크다운 형식으로 문단을 잘 구분해서"}
]
generated_text = generate_blog_post(messages)

if generated_text:
    print("생성된 블로그 글:")
    print(generated_text)
else:
    print("텍스트 생성에 실패했습니다.")

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )
# prompt = '한글로 답변해줘'
# print(completion.choices[0].message)
