import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Tạo mô hình sentence transformer
embedder = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Tạo cơ sở dữ liệu văn bản
documents = [
    "Hồ Chí Minh là một nhà cách mạng và Chủ tịch nước đầu tiên của Việt Nam.",
    "Trí tuệ nhân tạo (AI) đang thay đổi cách con người làm việc.",
    "RAG là mô hình kết hợp giữa truy xuất thông tin và tạo ngôn ngữ.",
    "FAISS là thư viện mã nguồn mở dùng để tìm kiếm vector hiệu quả.",
]

# Tạo embedding cho các văn bản
doc_embeddings = embedder.encode(documents)

# Tạo FAISS index
dimension = doc_embeddings[0].shape[0]  # số chiều của vector embedding
index = faiss.IndexFlatL2(dimension)
index.add(np.array(doc_embeddings))  # Thêm embedding vào index

# Lưu index vào file (nếu cần)
faiss.write_index(index, 'document_index.index')
