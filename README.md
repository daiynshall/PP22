Practice 09: Game Development with Pygame - Part 1
1. Objective
This practice introduces game development using Pygame. You will learn graphics, input handling, and animations by creating three classic games. This part focuses on basic concepts and implementation.

2. Resources and Learning
Start with the following tutorials:

🔗 Nerd Paradise Pygame Tutorial: https://nerdparadise.com/programming/pygame

Topics to Study:

Getting Started with Pygame
Working with Images
Music and Sound Effects
Geometric Drawing
Fonts and Text
More on Input (Keyboard, Mouse, Joystick)
3. Tasks
3.1 Mickey's Clock Application
Objective: Create a digital-style clock using Mickey Mouse hand graphics

Requirements:

Display current system time (minutes and seconds only)
Use Mickey Mouse's hands as clock hands
Right hand = minutes hand
Left hand = seconds hand
Synchronize with system clock in real-time
Update display every second
Implementation Tips:

Use pygame.transform.rotate() to rotate hands
Reference: StackOverflow - Rotating Graphics
Calculate rotation angles based on current time
Handle edge cases (leap seconds, etc.)
Repository Structure:

Practice7/
├── mickeys_clock/
│   ├── main.py
│   ├── clock.py
│   ├── images/
│   │   └── mickey_hand.png
│   └── README.md
3.2 Music Player with Keyboard Controller
Objective: Build an interactive music player with keyboard controls

Requirements:

Play/Stop/Next/Previous tracks with keyboard commands
Display current track information
Show playback progress or track position
Handle playlist management
Keyboard Controls Example:

P = Play
S = Stop
N = Next track
B = Previous (Back)
Q = Quit
Implementation Tips:

Use pygame.mixer for audio playback
Load multiple MP3/WAV files
Track current playlist position
Display UI with pygame.font
Repository Structure:

Practice7/
├── music_player/
│   ├── main.py
│   ├── player.py
│   ├── music/
│   │   ├── track1.wav
│   │   └── track2.wav
│   └── README.md
3.3 Moving Ball Game
Objective: Create an interactive game with a moving red ball

Requirements:

Display a red ball (50x50 pixels, radius 25) on white background
Move ball with arrow keys (Up, Down, Left, Right)
Each key press moves ball by 20 pixels
Ball cannot leave the screen boundaries
Ignore input that would move ball off-screen
Implementation Tips:

Use pygame.draw.circle() for the ball
Handle keyboard events
Check boundary conditions before moving
Smooth animation with frame rate control
Repository Structure:

Practice7/
├── moving_ball/
│   ├── main.py
│   ├── ball.py
│   └── README.md
3.4 Save to GitHub
Complete Repository Structure:

Practice7/
├── mickeys_clock/
│   ├── main.py
│   ├── clock.py
│   ├── images/
│   │   └── mickey_hand.png
│   └── README.md
├── music_player/
│   ├── main.py
│   ├── player.py
│   ├── music/
│   │   └── sample_tracks/
│   └── README.md
├── moving_ball/
│   ├── main.py
│   ├── ball.py
│   └── README.md
├── requirements.txt
└── README.md
Commit Instructions:

# Create requirements.txt
echo "pygame>=2.0.0" > requirements.txt

git add .
git commit -m "Add Practice7 - Pygame games: Mickey's clock, music player, moving ball"
git push origin main
4. What You Must Complete?
To pass this practice, you must:

✅ Complete Mickey's Clock application with working clock hands
✅ Implement Music Player with all keyboard controls
✅ Create Moving Ball game with boundary checking
✅ Code must be well-commented and organized
✅ All three games must run without errors
✅ Push all code to GitHub with clear commit messages
Deadline: check MS Teams announcements

5. 🛠 Troubleshooting
If you encounter issues:

Pygame Installation: pip install pygame
Image/Sound Loading: Verify file paths and formats
Rotation Issues: Check angle calculation (0° = up, clockwise positive)
Event Handling: Use pygame.event.get() correctly
Performance: Check frame rate and event loop frequency
6. Resources
📚 Nerd Paradise Pygame Tutorial
📚 Pygame Official Documentation
📚 Pygame Tutorials
💻 Pygame GitHub
🔧 StackOverflow - Pygame Rotation
📚 Real Python - Pygame Primer
