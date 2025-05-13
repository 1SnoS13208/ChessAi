import chess

class ChessAI:
    def __init__(self, color):
        self.color = color
        self.total_moves_checked = 0
        self.total_pruned_branches = 0
        
        # Piece-Square Tables (Evaluation Matrices)
        self.pawn_eval_white = [
            [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
            [5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0],
            [1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0],
            [0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5],
            [0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0],
            [0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5],
            [0.5,  1.0,  1.0, -2.0, -2.0,  1.0,  1.0,  0.5],
            [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]
        ]
        
        self.pawn_eval_black = self._reverse_array(self.pawn_eval_white)
        
        self.knight_eval_white = [
            [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
            [-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0],
            [-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0],
            [-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0],
            [-3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0],
            [-3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0],
            [-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0],
            [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
        ]
        
        self.knight_eval_black = self._reverse_array(self.knight_eval_white)
        
        self.bishop_eval_white = [
            [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
            [-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
            [-1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0],
            [-1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0],
            [-1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0],
            [-1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0],
            [-1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0],
            [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
        ]
        
        self.bishop_eval_black = self._reverse_array(self.bishop_eval_white)
        
        self.rook_eval_white = [
            [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
            [0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5],
            [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
            [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
            [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
            [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
            [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
            [0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0]
        ]
        
        self.rook_eval_black = self._reverse_array(self.rook_eval_white)
        
        self.queen_eval_white = [
            [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
            [-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
            [-1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
            [-0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
            [0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
            [-1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
            [-1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
            [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
        ]
        
        self.queen_eval_black = self._reverse_array(self.queen_eval_white)
        
        self.king_eval_white = [
            [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
            [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
            [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
            [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
            [-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
            [-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
            [2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0],
            [2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0]
        ]
        
        self.king_eval_black = self._reverse_array(self.king_eval_white)

    def _reverse_array(self, array):
        """Reverse the evaluation matrix for black pieces."""
        return array[::-1]

    def _get_piece_value(self, piece):
        """Assign base value to different pieces."""
        values = {
            chess.PAWN: 10.0,
            chess.KNIGHT: 30.0,
            chess.BISHOP: 30.0,
            chess.ROOK: 50.0,
            chess.QUEEN: 90.0,
            chess.KING: 900.0
        }
        return values.get(piece, 0.0)

    def _get_piece_square_value(self, piece, square, color):
        """Get positional value for a piece based on its square."""
        row, col = chess.square_rank(square), chess.square_file(square)
        
        # Adjust row/col based on color
        if color == chess.BLACK:
            row = 7 - row
        
        # Select appropriate evaluation matrix
        if piece == chess.PAWN:
            eval_matrix = self.pawn_eval_white if color == chess.WHITE else self.pawn_eval_black
        elif piece == chess.KNIGHT:
            eval_matrix = self.knight_eval_white if color == chess.WHITE else self.knight_eval_black
        elif piece == chess.BISHOP:
            eval_matrix = self.bishop_eval_white if color == chess.WHITE else self.bishop_eval_black
        elif piece == chess.ROOK:
            eval_matrix = self.rook_eval_white if color == chess.WHITE else self.rook_eval_black
        elif piece == chess.QUEEN:
            eval_matrix = self.queen_eval_white if color == chess.WHITE else self.queen_eval_black
        elif piece == chess.KING:
            eval_matrix = self.king_eval_white if color == chess.WHITE else self.king_eval_black
        else:
            return 0.0
        
        return eval_matrix[row][col]

    def evaluate_board(self, board):
        """Evaluate the current board state."""
        if board.is_checkmate():
            return float('-inf') if board.turn == self.color else float('inf')
        
        if board.is_stalemate() or board.is_insufficient_material():
            return 0.0
        
        total_evaluation = 0.0
        
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece is not None:
                # Determine sign based on piece color
                sign = 1 if piece.color == self.color else -1
                
                # Calculate piece value
                piece_value = self._get_piece_value(piece.piece_type)
                piece_square_value = self._get_piece_square_value(piece.piece_type, square, piece.color)
                
                total_evaluation += sign * (piece_value + piece_square_value)
        
        return total_evaluation

    def minimax(self, board, depth, maximizing_player, alpha=float('-inf'), beta=float('inf')):
        """Minimax algorithm with alpha-beta pruning."""
        if depth == 0 or board.is_game_over():
            return self.evaluate_board(board)
        
        if maximizing_player:
            max_eval = float('-inf')
            for move in board.legal_moves:
                board.push(move)
                self.total_moves_checked += 1
                eval = self.minimax(board, depth - 1, False, alpha, beta)
                board.pop()
                
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    self.total_pruned_branches += 1
                    break  # Beta cut-off
            return max_eval
        else:
            min_eval = float('inf')
            for move in board.legal_moves:
                board.push(move)
                self.total_moves_checked += 1
                eval = self.minimax(board, depth - 1, True, alpha, beta)
                board.pop()
                
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    self.total_pruned_branches += 1
                    break  # Alpha cut-off
            return min_eval

    def get_best_move(self, board, depth=3):
        """Find the best move using minimax algorithm with alpha-beta pruning."""
        self._reset_move_stats()
        best_moves = []  # List to store all moves with the same best score
        max_eval = float('-inf')
        alpha = float('-inf')
        beta = float('inf')
        
        for move in board.legal_moves:
            board.push(move)
            self.total_moves_checked += 1
            move_eval = self._minimax_with_stats(board, depth - 1, False, alpha, beta)
            board.pop()
            
            if move_eval > max_eval:
                max_eval = move_eval
                best_moves = [move]  # Reset list with new best move
            elif move_eval == max_eval:
                best_moves.append(move)  # Add equally good move
            
            alpha = max(alpha, move_eval)
        
        self._log_move_stats()
        
        # Return the first best move found
        return best_moves[0] if best_moves else None

    def _sort_moves_by_score(self, board, moves, maximizing_player):
        """Sort moves by score to prune more efficiently"""
        move_scores = []
        for move in moves:
            board.push(move)
            score = self.evaluate_board(board)
            board.pop()
            move_scores.append((move, score))
        
        # Sort in descending order if maximizing, ascending order if minimizing
        return [move for move, _ in sorted(move_scores, key=lambda x: x[1], reverse=maximizing_player)]

    def _minimax_with_stats(self, board, depth, maximizing_player, alpha=float('-inf'), beta=float('inf')):
        """Minimax algorithm with alpha-beta pruning and move tracking."""
        if depth == 0 or board.is_game_over():
            return self.evaluate_board(board)
        
        moves = list(board.legal_moves)
        # Sort moves by score
        moves = self._sort_moves_by_score(board, moves, maximizing_player)
        
        if maximizing_player:
            max_eval = float('-inf')
            for move in moves:
                board.push(move)
                self.total_moves_checked += 1
                eval = self._minimax_with_stats(board, depth - 1, False, alpha, beta)
                board.pop()
                
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                
                # Pruning condition
                if beta <= alpha:
                    self.total_pruned_branches += len(moves) - moves.index(move) - 1
                    break  # Beta cut-off
            return max_eval
        else:
            min_eval = float('inf')
            for move in moves:
                board.push(move)
                self.total_moves_checked += 1
                eval = self._minimax_with_stats(board, depth - 1, True, alpha, beta)
                board.pop()
                
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                
                # Pruning condition
                if beta <= alpha:
                    self.total_pruned_branches += len(moves) - moves.index(move) - 1
                    break  # Alpha cut-off
            return min_eval

    def _reset_move_stats(self):
        self.total_moves_checked = 0
        self.total_pruned_branches = 0

    def _log_move_stats(self):
        print(f'Total moves checked: {self.total_moves_checked}')
        print(f'Total pruned branches: {self.total_pruned_branches}')

    def choose_move(self, board):
        """Choose a move for the AI."""
        return self.get_best_move(board)
