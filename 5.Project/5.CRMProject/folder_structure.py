import os

def generate_folder_structure(root_path, output_file="folder_structure.txt"):
    # 제외할 폴더와 파일들
    exclude_folders = {
        "__pycache__",
        ".git", 
        "node_modules",
        ".vscode",
        "venv",
        ".env",
        ".pytest_cache",
        "build",
        "dist",
        ".idea",
        "target"
    }
    
    exclude_files = {
        ".DS_Store",
        "Thumbs.db",
        "*.log",
        ".gitignore"
    }
    
    exclude_extensions = {
        ".pyc",
        ".pyo",
        ".pyd",
        ".log",
        ".tmp"
    }
    
    def should_exclude(name, is_dir=False):
        # 폴더 제외 확인
        if is_dir and name in exclude_folders:
            return True
        
        # 파일 제외 확인
        if not is_dir:
            if name in exclude_files:
                return True
            
            # 확장자 체크
            _, ext = os.path.splitext(name)
            if ext in exclude_extensions:
                return True
        
        # 숨김 파일/폴더 (선택사항)
        if name.startswith('.') and name not in ['.gitignore', '.env']:
            return True
            
        return False
    
    def print_tree(path, prefix="", file_obj=None, show_files=True):
        try:
            items = []
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                is_dir = os.path.isdir(item_path)
                
                if not should_exclude(item, is_dir):
                    items.append((item, is_dir, item_path))
            
            # 정렬: 폴더 먼저, 그 다음 파일
            items.sort(key=lambda x: (not x[1], x[0].lower()))
            
            for i, (item, is_dir, item_path) in enumerate(items):
                is_last = (i == len(items) - 1)
                
                # 트리 구조 문자
                if is_last:
                    current_prefix = "└── "
                    next_prefix = prefix + "    "
                else:
                    current_prefix = "├── "
                    next_prefix = prefix + "│   "
                
                # 아이콘 추가
                if is_dir:
                    icon = "📁 "
                else:
                    # 파일 확장자별 아이콘
                    ext = os.path.splitext(item)[1].lower()
                    icon_map = {
                        '.py': '🐍 ',
                        '.html': '🌐 ',
                        '.css': '🎨 ',
                        '.js': '📜 ',
                        '.json': '📋 ',
                        '.md': '📝 ',
                        '.txt': '📄 ',
                        '.db': '🗄️ ',
                        '.sql': '🗃️ '
                    }
                    icon = icon_map.get(ext, '📄 ')
                
                line = f"{prefix}{current_prefix}{icon}{item}"
                
                print(line)
                if file_obj:
                    file_obj.write(line + "\n")
                
                # 재귀적으로 하위 폴더 탐색
                if is_dir:
                    print_tree(item_path, next_prefix, file_obj, show_files)
                    
        except PermissionError:
            error_line = f"{prefix}[접근 권한 없음]"
            print(error_line)
            if file_obj:
                file_obj.write(error_line + "\n")
    
    # 실행
    print(f"📂 {os.path.basename(root_path)} 폴더 구조 생성 중...")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        header = f"📂 {os.path.basename(root_path)} 폴더 구조\n"
        header += "=" * 50 + "\n\n"
        
        print(header.strip())
        f.write(header)
        
        # 루트 폴더 표시
        root_line = f"📁 {os.path.basename(root_path)}/\n"
        print(root_line.strip())
        f.write(root_line)
        
        # 트리 구조 생성
        print_tree(root_path, "", f)
        
        footer = f"\n\n생성 완료: {output_file}"
        print(footer)
        # f.write(footer)

# 사용법
if __name__ == "__main__":
    # 현재 폴더 구조 생성
    current_path = os.getcwd()
    generate_folder_structure(current_path, "folder_structure.txt")
