from openai import OpenAI
client = OpenAI()

def generate_blog_post(topic):
    try:
        # 사용자 입력을 prompt로 설정
        prompt = f"주제: {topic}"
        
        # OpenAI API를 사용하여 텍스트 생성 요청
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # 적절한 모델 선택
            prompt=prompt,
            max_tokens=30,  # 생성할 최대 토큰 수
            stop=None
        )

        # 생성된 텍스트 반환
        return response.choices[0].text.strip()

    except Exception as e:
        print(f"Error: {e}")
        return None
topic = 'chat gpt로 자동화 블로그 글을 썻다는 내용'
generated_text = generate_blog_post(topic)
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
