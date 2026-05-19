import cv2
import math

class VideoMeasurer:
    def __init__(self, video_path):
        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)
        
        if not self.cap.isOpened():
            print(f"Error: Could not open video file {video_path}")
            return

        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.window_name = "Video Distance Measurer"
        self.current_frame_idx = 0
        self.points = []
        
        # Setup GUI
        cv2.namedWindow(self.window_name)
        cv2.createTrackbar("Frame", self.window_name, 0, self.total_frames - 1, self.on_trackbar_change)
        cv2.setMouseCallback(self.window_name, self.on_mouse_click)

    def on_trackbar_change(self, val):
        """Update current frame index when slider moves."""
        self.current_frame_idx = val

    def on_mouse_click(self, event, x, y, flags, param):
        """Handle mouse clicks to select two points."""
        if event == cv2.EVENT_LBUTTONDOWN:
            # If we already have two points, reset for a new measurement
            if len(self.points) >= 2:
                self.points = []
            
            self.points.append((x, y))
            print(f"Point added: ({x}, {y})")

    def calculate_distance(self, p1, p2):
        """Calculate Euclidean distance between two points."""
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    def run(self):
        print("Instructions:")
        print("- Click two points to measure distance.")
        print("- Use the slider or Left/Right arrow keys to navigate frames.")
        print("- Press 'R' to clear points.")
        print("- Press 'Q' or 'ESC' to quit.")

        while True:
            # Seek to the current frame index
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.current_frame_idx)
            ret, frame = self.cap.read()
            
            if not ret:
                # If video ends or frame fails, stay at last known good frame or loop
                self.current_frame_idx = 0
                continue

            display_frame = frame.copy()

            # Draw measurement logic
            for p in self.points:
                cv2.circle(display_frame, p, 5, (0, 0, 255), -1)
            
            if len(self.points) == 2:
                p1, p2 = self.points[0], self.points[1]
                cv2.line(display_frame, p1, p2, (0, 255, 0), 2)
                
                dist = self.calculate_distance(p1, p2)
                mid_point = ((p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2)
                
                # Display distance text
                text = f"{dist:.2f} px"
                cv2.putText(display_frame, text, mid_point, 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

            cv2.imshow(self.window_name, display_frame)
            
            # Sync trackbar position with current_frame_idx (in case updated by keys)
            cv2.setTrackbarPos("Frame", self.window_name, self.current_frame_idx)

            # waitKeyEx handles arrow keys better on many platforms
            key = cv2.waitKeyEx(30)

            # Navigation and controls
            if key in [27, ord('q'), ord('Q')]:  # ESC or Q to quit
                break
            elif key == ord('r') or key == ord('R'):
                self.points = []
            # Arrow Keys (Note: Codes can vary slightly by OS, these are common for OpenCV)
            elif key == 2555904 or key == 65363 or key == ord('d'): # Right Arrow / 'd'
                self.current_frame_idx = min(self.total_frames - 1, self.current_frame_idx + 1)
            elif key == 2424832 or key == 65361 or key == ord('a'): # Left Arrow / 'a'
                self.current_frame_idx = max(0, self.current_frame_idx - 1)

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # Replace 'video.mp4' with your actual video file path
    VIDEO_PATH = "MVI_0012.MP4"
    app = VideoMeasurer(VIDEO_PATH)
    app.run()
