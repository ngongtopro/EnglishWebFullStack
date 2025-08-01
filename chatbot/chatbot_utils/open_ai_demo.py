import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import openai  # Hoặc thay bằng model local nếu cần
from chatbot.chatbot_utils.constances import OPEN_AI_API_KEY
from openai import OpenAI

# 1. Cấu hình OpenAI (thay bằng mô hình khác nếu bạn dùng local model)
openai.api_key = OPEN_AI_API_KEY

# 2. Khởi tạo embedding model
embedder = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# 3. Cơ sở dữ liệu văn bản (có thể thay bằng file txt, PDF, v.v.)
documents = [
    "Hồ Chí Minh là một nhà cách mạng và Chủ tịch nước đầu tiên của Việt Nam.",
    "Trí tuệ nhân tạo (AI) đang thay đổi cách con người làm việc.",
    "RAG là mô hình kết hợp giữa truy xuất thông tin và tạo ngôn ngữ.",
    "FAISS là thư viện mã nguồn mở dùng để tìm kiếm vector hiệu quả.",
]

# 4. Tạo vector embeddings và xây FAISS index
doc_embeddings = embedder.encode(documents)
dimension = doc_embeddings[0].shape[0]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(doc_embeddings))

client = OpenAI(api_key=OPEN_AI_API_KEY)

query = 'quit1'
while query != 'quit':
    # 5. Nhận truy vấn từ người dùng
    query = input("Nhập câu hỏi của bạn: ")
    response = client.chat.completions.create(
        model="gpt-4o",
        instructions="You are a coding assistant that talks like a pirate.",
        input=query
    )
    query_embedding = embedder.encode([query])
    k = 2  # số lượng văn bản gần nhất
    _, indices = index.search(np.array(query_embedding), k)

    # 6. Lấy văn bản phù hợp
    retrieved_docs = [documents[i] for i in indices[0]]
    context = "\n".join(retrieved_docs)

    # 7. Gửi prompt cho mô hình LLM (ở đây dùng GPT-3.5)
    prompt = f"""
    Bạn là một trợ lý thông minh. Dưới đây là một số thông tin tham khảo:

    {context}

    Dựa trên các thông tin trên, trả lời câu hỏi: "{query}"
    """

    # 8. Gọi OpenAI GPT
    response = openai.completions.create(
        model="gpt-3.5-turbo",  # hoặc "gpt-4", "gpt-4o"
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    print("\n📌 Câu trả lời:")
    print(response['choices'][0]['message']['content'])
