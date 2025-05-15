from main import Main

def launch(ai_mode=True, depth=3, alpha_beta=True):
    """
    Launch the chess game with custom parameters.
    
    Parameters:
        ai_mode (bool): True to play against AI, False for two human players
        depth (int): AI search depth (1-7), higher values make AI stronger but slower
        alpha_beta (bool): True to use Minimax with Alpha-Beta pruning, False for standard Minimax
    """    
    app = Main(ai_mode=ai_mode)
    app.ai_depth = depth
    app.use_alpha_beta = alpha_beta
    app.mainloop()

if __name__ == "__main__":
    # Configure parameters here
    launch(ai_mode=True, depth=3, alpha_beta=True)
