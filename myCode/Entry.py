from tkinter import Tk, Canvas, Entry, Button, PhotoImage
from typing import Optional
from dataclasses import dataclass
from pathlib import Path

@dataclass
class ViewerConfig:
    """Configuration for the image viewer window."""
    width: int = 640
    height: int = 480
    bg_color: str = "#808080"

class ImageViewer:
    """Simple image viewer application using tkinter."""
    
    def __init__(self, config: ViewerConfig = ViewerConfig()) -> None:
        """Initialize the image viewer window and widgets.
        
        Args:
            config: Configuration object for window settings
        """
        self.root = Tk()
        self.root.title("Image Viewer")
        
        # Initialize widgets
        self.canvas = Canvas(
            self.root,
            width=config.width,
            height=config.height,
            bg=config.bg_color
        )
        self.entry = Entry(self.root)
        self.show_button = Button(
            self.root,
            text="Show",
            command=self.display_image
        )
        
        # Layout widgets
        self.canvas.pack()
        self.entry.pack()
        self.show_button.pack()
        
        # Store the PhotoImage reference to prevent garbage collection
        self.current_image: Optional[PhotoImage] = None
        
    def display_image(self) -> None:
        """Load and display the image from the path specified in the entry field."""
        file_path = self.entry.get()
        
        try:
            # Ensure the file path is valid
            if not Path(file_path).is_file():
                print(f"Error: File not found - {file_path}")
                return
                
            # Load and display the image
            self.current_image = PhotoImage(file=file_path)
            self.canvas.create_image(
                0, 0,
                anchor="nw",
                image=self.current_image
            )
            
        except Exception as e:
            print(f"Error loading image: {e}")
            
    def run(self) -> None:
        """Start the application main loop."""
        self.root.mainloop()

def main() -> None:
    """Entry point of the application."""
    viewer = ImageViewer()
    viewer.run()

if __name__ == "__main__":
    main()