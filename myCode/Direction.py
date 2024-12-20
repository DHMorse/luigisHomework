from tkinter import Tk, Canvas, Event
from dataclasses import dataclass

@dataclass
class GameObject:
    """Represents a game object with position and velocity."""
    canvas_id: int
    xvel: float = 0.0
    yvel: float = 0.0

class DirectionGame:
    """Main game class handling the movement mechanics and window setup."""
    
    def __init__(self, width: int = 1000, height: int = 1000) -> None:
        """Initialize the game window and game object.
        
        Args:
            width: Window width in pixels
            height: Window height in pixels
        """
        self.root = Tk()
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        
        # Create the player rectangle
        rect_id = self.canvas.create_rectangle(
            50, 50, 60, 60,
            width=2,
            outline="#880000"
        )
        self.player = GameObject(canvas_id=rect_id)
        
        # Bind keyboard controls
        self._setup_controls()
        
    def _setup_controls(self) -> None:
        """Bind keyboard events to their respective handlers."""
        key_bindings = {
            "<KeyPress-Left>": self.change_speed,
            "<KeyPress-Right>": self.change_speed,
            "<KeyPress-Up>": self.change_speed,
            "<KeyPress-Down>": self.change_speed,
            "<KeyPress-s>": self.change_speed
        }
        
        for key, handler in key_bindings.items():
            self.canvas.bind_all(key, handler)
            
    def change_speed(self, event: Event) -> None:
        """Handle keyboard events to change the player's velocity.
        
        Args:
            event: Keyboard event containing the key pressed
        """
        SPEED_CHANGE: float = 0.4
        
        match event.keysym:
            case "Left":
                self.player.xvel -= SPEED_CHANGE
            case "Right":
                self.player.xvel += SPEED_CHANGE
            case "Up":
                self.player.yvel -= SPEED_CHANGE
            case "Down":
                self.player.yvel += SPEED_CHANGE
            case "s":
                self.player.xvel = 0.0
                self.player.yvel = 0.0
                
    def move_rectangle(self) -> None:
        """Update the player's position and schedule the next update."""
        self.canvas.move(
            self.player.canvas_id,
            self.player.xvel,
            self.player.yvel
        )
        self.canvas.after(20, self.move_rectangle)
        
    def run(self) -> None:
        """Start the game loop."""
        self.move_rectangle()
        self.root.mainloop()

def main() -> None:
    """Entry point of the application."""
    game = DirectionGame()
    game.run()

if __name__ == "__main__":
    main()