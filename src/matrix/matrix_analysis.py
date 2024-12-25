class MatrixAnalysis:
    @staticmethod
    def sum(matrix: list[list[int]]) -> int:
        result = 0
        for row in matrix:
            for number in row:
                result += number
        return result

    @staticmethod
    def max(matrix: list[list[int]]) -> int:
        max_number = matrix[0][0]
        for row in matrix:
            for number in row:
                if number > max_number:
                    max_number = number
        return max_number

    @staticmethod
    def min(matrix: list[list[int]]) -> int:
        min_number = matrix[0][0]
        for row in matrix:
            for number in row:
                if number < min_number:
                    min_number = number
        return min_number

    @staticmethod
    def mode(matrix: list[list[int]]) -> int:
        numbers_count = {}
        for row in matrix:
            for number in row:
                # if number in numbers_count:
                #     numbers_count[number] += 1
                # else:
                #     numbers_count[number] = 1
                numbers_count[number] = numbers_count.get(number, 0) + 1
        max_frequency = 0
        max_frequency_number = matrix[0][0]
        for number, frequency in numbers_count.items():
            if frequency > max_frequency:
                max_frequency = frequency
                max_frequency_number = number
        return max_frequency_number

