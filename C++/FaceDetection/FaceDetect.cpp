#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/objdetect.hpp>

#include <iostream>

using namespace cv;
using namespace std;

int main()
{
    // Default webcam
    VideoCapture video(0);
    CascadeClassifier faceDetect;
    Mat img;

    // Load the face detection classifier
    faceDetect.load("C:\\Users\\aiden\\Downloads\\haarcascade_frontalface_default.xml");


    //If there is no file then return 
    if (faceDetect.empty()) 
    {
        cerr << "Error: Unable to load face detection classifier." << endl;
        return -1;
    }

    while (true)
    {
        video.read(img);

        // Creates a vector to store all of the faces
        vector<Rect> faces;

        // Detect faces in the frame
        faceDetect.detectMultiScale(img, faces, 1.3, 5);

        int numFaces = faces.size();

        for (size_t i = 0; i < faces.size(); i++)
        {
            // Draw rectangles around detected faces
            rectangle(img, faces[i].tl(), faces[i].br(), Scalar(50, 20, 255), 3);
        }

        putText(img, "Number of Faces: " + to_string(numFaces), Point(10, 30), FONT_HERSHEY_DUPLEX, 1, Scalar(0, 255, 0), 2);

        imshow("Frame", img);
        int key = waitKey(1);

        if (key == 27) {  // Press 'Esc' key to exit
            break;
        }
    }

    return 0;
}
