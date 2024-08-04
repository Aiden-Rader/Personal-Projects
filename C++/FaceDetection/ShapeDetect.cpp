#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>

int main2() {
    cv::VideoCapture cap(0); // Open the default webcam (change the argument for a different camera)

    if (!cap.isOpened()) {
        std::cerr << "Error: Unable to access the webcam." << std::endl;
        return -1;
    }

    while (true) {
        cv::Mat frame;
        cap >> frame; // Capture a frame from the webcam

        // Convert the frame to grayscale
        cv::Mat gray;
        cv::cvtColor(frame, gray, cv::COLOR_BGR2GRAY);

        // Apply Gaussian blur to reduce noise
        cv::GaussianBlur(gray, gray, cv::Size(5, 5), 0);

        // Detect edges using Canny
        cv::Mat edges;
        cv::Canny(gray, edges, 50, 150);

        // Find contours in the edges image
        std::vector<std::vector<cv::Point>> contours;
        cv::findContours(edges, contours, cv::RETR_EXTERNAL, cv::CHAIN_APPROX_SIMPLE);

        // Loop over the detected contours
        for (size_t i = 0; i < contours.size(); i++) {
            // Approximate the contour to simplify it
            double epsilon = 0.04 * cv::arcLength(contours[i], true);
            std::vector<cv::Point> approx;
            cv::approxPolyDP(contours[i], approx, epsilon, true);

            // Get the number of vertices
            int numVertices = static_cast<int>(approx.size());

            // Classify the shape based on the number of vertices
            std::string shape = "Unidentified";

            if (numVertices == 3) {
                shape = "Triangle";
            }
            else if (numVertices == 4) {
                cv::Rect boundingBox = cv::boundingRect(contours[i]);
                float aspectRatio = static_cast<float>(boundingBox.width) / boundingBox.height;
                if (aspectRatio >= 0.95 && aspectRatio <= 1.05) {
                    shape = "Square";
                }
                else {
                    shape = "Rectangle";
                }
            }
            else if (numVertices >= 10) {
                shape = "Circle";
            }

            // Draw the shape name on the frame
            cv::Moments mu = cv::moments(contours[i]);
            int cX = static_cast<int>(mu.m10 / mu.m00);
            int cY = static_cast<int>(mu.m01 / mu.m00);
            cv::putText(frame, shape, cv::Point(cX, cY), cv::FONT_HERSHEY_SIMPLEX, 0.5, cv::Scalar(0, 0, 255), 2);
            cv::drawContours(frame, contours, static_cast<int>(i), cv::Scalar(0, 255, 0), 2);
        }

        // Display the frame with shape names
        cv::imshow("Shapes", frame);

        // Press 'Esc' key to exit
        if (cv::waitKey(1) == 27) {
            break;
        }
    }

    cap.release();
    cv::destroyAllWindows();

    return 0;
}
