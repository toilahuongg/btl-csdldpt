from db import createTable, createCharacter

def setup(): 
  # Tạo table
  createTable()

  # dữ liệu

  # Nhân vật Aladdin Abu
  createCharacter(name='Aladdin Abu', folder='aladdin-abu', desc='''
  Abu là chú khỉ đồng hành và người bạn thân thiết của Aladdin trong bộ phim hoạt hình Disney "Aladdin". Màu sắc chủ đạo của nhân vật Abu trong hoạt hình Aladdin là màu nâu. Abu có bộ lông nâu và mặc trang phục nâu như một chiếc áo choàng và mũ có ren màu nâu. 
  ''')

  # Nhân vật Aladdin Genie
  createCharacter(name='Aladdin Genie', folder='aladdin-genie', desc='Genie là một vị thần có khả năng biến hóa và thực hiện ba điều ước cho người sở hữu chiếc đèn ma thuật.Màu sắc chủ đạo của nhân vật Genie trong hoạt hình Aladdin là màu xanh. Genie có da màu xanh và mặc trang phục xanh lá cây, thường là một chiếc áo choàng dài màu xanh với dải vàng. ')

  # Nhân vật Daisyduck
  createCharacter(name='Daisyduck', folder='daisyduck', desc='Daisy Duck là một nhân vật phụ trong loạt phim hoạt hình của Disney')

  # Nhân vật Donaldduck
  createCharacter(name='Donaldduck', folder='donaldduck', desc='Donald Duck là một nhân vật nổi tiếng trong loạt phim hoạt hình và truyện tranh của Disney')

  # Nhân vật Eeyore
  createCharacter(name='Eeyore', folder='eeyore', desc='Eeyore là một nhân vật trong bộ truyện "Winnie the Pooh" của nhà văn A.A. Milne')

  # Nhân vật Fawn
  createCharacter(name='Fawn', folder='fawn', desc='Fawn là một nhân vật trong loạt phim hoạt hình Disney "Tinker Bell" (Công chúa Tinker Bell) và các phần mở rộng của nó')

  # Nhân vật Jasmine
  createCharacter(name='Jasmine', folder='jasmine', desc='Jasmine là nhân vật nữ chính trong bộ phim hoạt hình Disney "Aladdin"')

  # Nhân vật Mickey
  createCharacter(name='Mickey', folder='mickey', desc='Mickey Mouse là một nhân vật biểu tượng của Disney và là một trong những nhân vật hoạt hình nổi tiếng nhất trên thế giới')

  # Nhân vật Pluto
  createCharacter(name='Pluto', folder='pluto', desc='Pluto là một nhân vật trong loạt phim hoạt hình Disney và là chú chó trung thành của Mickey Mouse')

  # Nhân vật Pooh
  createCharacter(name='Pooh', folder='pooh', desc='Pooh là một nhân vật chính trong loạt truyện tranh và phim hoạt hình "Winnie the Pooh" của nhà văn A.A. Milne')

  # Nhân vật Rabbit
  createCharacter(name='Rabbit', folder='rabbit', desc='Rabbit là một nhân vật trong loạt truyện tranh và phim hoạt hình "Winnie the Pooh" của nhà văn A.A')

  # Nhân vật Tiger
  createCharacter(name='Tiger', folder='tiger', desc='Tiger (hoặc Tigger) là một nhân vật trong loạt truyện tranh và phim hoạt hình "Winnie the Pooh" của nhà văn A.A. Milne')
