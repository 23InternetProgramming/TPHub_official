from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view()),  # navbar의 게시물 탭 (= 전체 게시물)
    path('category/', views.CategoryList.as_view()),  # 카테고리 종류 4개 보일 화면
    path('category/<str:slug>/', views.category_post),  # 해당 카테고리로 쓰여진 모든 글 목록
    path('<int:pk>/', views.PostDetail.as_view()),  # 글 상세보기
    path('create_post/', views.PostCreate.as_view()),  # 글 생성
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),  # 글 수정
    path('delete_post/<int:pk>/', views.PostDelete.as_view()),  # 글 삭제
    path('<int:pk>/new_comment/', views.new_comment),  # 댓글 추가
    path('delete_comment/<int:pk>/', views.delete_comment),  # 댓글 삭제
]

