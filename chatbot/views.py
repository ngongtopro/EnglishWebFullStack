from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .chatbot_utils.serializers import UserSerializer


content = []

@api_view(['GET', 'POST'])
def request_answer_view(request):
    if request.method == 'GET':
        data = {
                "role": 'assistant',
                "content": 'Đang dùng GET. Chưa có gì để trả về',
            }
        return Response(data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            content.append({
                "role": serializer.validated_data['role'],
                "content": serializer.validated_data['content'],
            })
            temp = {
                "role": 'assistant',
                "content": f'{serializer.validated_data['content']} đã tiếp nhận.',
            }
            print(temp)
            return Response(temp, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'DELETE'])
# def todo_detail(request, todo_id):
#     # Tìm todo theo ID
#     todo = next((todo for todo in todos if todo["id"] == todo_id), None)
    
#     if not todo:
#         return Response({"error": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = UserSerializer(todo)
#         return Response(serializer.data)
    
#     elif request.method == 'DELETE':
#         todos.remove(todo)
#         return Response(status=status.HTTP_204_NO_CONTENT)