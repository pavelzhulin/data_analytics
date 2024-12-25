from src.films.films_manager import FilmsManager

# matrix = [[5, 5, 3, 4],
#           [1, 2, 1, 5]
#           ]
# print(MatrixAnalysis.sum(matrix))
# print(MatrixAnalysis.max(matrix))
# print(MatrixAnalysis.min(matrix))
# print(MatrixAnalysis.mode(matrix))
manager = FilmsManager('films/films_db.json')
manager.load_db()

manager.manage()
# manager.save_db()
