from tkinter import Tk, Canvas, Event
from typing import Dict, Tuple
from dataclasses import dataclass

@dataclass
class GameObject:
    """Represents a game object with its canvas ID."""
    canvas_id: int

@dataclass
class GameConfig:
    """Configuration for the game window."""
    width: int = 600
    height: int = 400
    player_color: str = "#0000AA"
    player_width: int = 2
    move_distance: int = 10

class KeyboardGame:
    """Simple game with keyboard-controlled movement."""
    
    def __init__(self, config: GameConfig = GameConfig()) -> None:
        """Initialize the game window and player object.
        
        Args:
            config: Configuration object for game settings
        """
        self.config = config
        self.root = Tk()
        self.root.title("Keyboard Control")
        
        # Create canvas
        self.canvas = Canvas(
            self.root,
            width=config.width,
            height=config.height
        )
        self.canvas.pack()
        
        # Create player
        player_id = self.canvas.create_rectangle(
            10, 50, 20, 60,
            outline=config.player_color,
            width=config.player_width
        )
        self.player = GameObject(canvas_id=player_id)
        
        # Define movement vectors
        self.movement_vectors: Dict[str, Tuple[int, int]] = {
            "Left": (-self.config.move_distance, 0),
            "Right": (self.config.move_distance, 0),
            "Up": (0, -self.config.move_distance),
            "Down": (0, self.config.move_distance)
        }
        
        # Setup controls
        self._bind_controls()
        
    def _bind_controls(self) -> None:
        """Bind keyboard events to the move handler."""
        for key in self.movement_vectors.keys():
            self.canvas.bind_all(f"<KeyPress-{key}>", self.move)
            
    def move(self, event: Event) -> None:
        """Handle movement based on keyboard input.
        
        Args:
            event: Keyboard event containing the key pressed
        """
        if event.keysym in self.movement_vectors:
            dx, dy = self.movement_vectors[event.keysym]
            self.canvas.move(self.player.canvas_id, dx, dy)
            
    def run(self) -> None:
        """Start the game loop."""
        self.root.mainloop()

def main() -> None:
    """Entry point of the application."""
    game = KeyboardGame()
    game.run()

if __name__ == "__main__":
    main()