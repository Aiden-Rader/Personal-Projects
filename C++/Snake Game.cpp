#include <iostream>
#include <conio.h>
#include <windows.h>

using namespace std;

const int width = 20;
const int height = 10;

bool gameover;

int x, y, fruitX, fruitY, score = 0;
int tailX[100], tailY[100];
int nTail = 0;

enum eDirecton { STOP = 0, LEFT, RIGHT, UP, DOWN };
eDirecton dir;

void Setup()
{
    gameover = false;
    dir = STOP;
    x = width / 2;
    y = height / 2;

    //Seed the random number generator with the current time
    srand(static_cast<unsigned>(time(0)));

    fruitX = rand() % width;
    fruitY = rand() % height;
}

void ClearScreen() 
{
    // Use escape sequences to clear the screen
    cout << "\033[2J\033[H";
}

void Draw() 
{
    ClearScreen();

    for (int i = 0; i < width + 2; i++)
        cout << "-";
    cout << endl;

    //Draw the elements like the head, fruit, and tail
    for (int i = 0; i < height; i++) 
    {
        for (int j = 0; j < width; j++) 
        {
            if (j == 0 || j == width - 1)
                
                //Draw the side walls
                cout << "|";
            if (i == y && j == x)

                //Draw the snakes inital head
                cout << "O";
            else if (i == fruitY && j == fruitX)
                
                //Draw the fruit
                cout << "F";
            else 
            {
                bool print = false;
                for (int k = 0; k < nTail; k++) 
                {
                    if (tailX[k] == j && tailY[k] == i)
                    {
                        //Draw the snakes tail
                        cout << "o";
                        print = true;
                    }
                }
                if (!print)
                    //Draw empty spaces
                    cout << " ";
            }
        }
        cout << endl;
    }

    for (int i = 0; i < width + 2; i++)
        cout << "-"; //<- Draw bottom wall
    cout << endl;
    cout << "Score:" << score << endl;
}

//Function to handle user input
void Input() 
{
    if (_kbhit()) 
    {
        switch (_getch()) 
        {
        case 'a':
            dir = LEFT;
            break;
        case 'd':
            dir = RIGHT;
            break;
        case 'w':
            dir = UP;
            break;
        case 's':
            dir = DOWN;
            break;
        case 'x':
            gameover = true;
            break;
        }
    }
}

void Logic() 
{
    //Update snakes tail position
    int prevX = tailX[0];
    int prevY = tailY[0];
    int prev2X, prev2Y;
    tailX[0] = x;
    tailY[0] = y;

    for (int i = 1; i < nTail; i++) 
    {
        prev2X = tailX[i];
        prev2Y = tailY[i];
        tailX[i] = prevX;
        tailY[i] = prevY;
        prevX = prev2X;
        prevY = prev2Y;
    }

    //Move the snake based on the current direction
    switch (dir) 
    {
    case LEFT:
        x--;
        break;
    case RIGHT:
        x++;
        break;
    case UP:
        y--;
        break;
    case DOWN:
        y++;
        break;
    }

    //Check for collision with walls and collision with the snakes tail
    if (x < 0 || x >= width || y < 0 || y >= height)
        gameover = true;

    for (int i = 0; i < nTail; i++) 
    {
        if (tailX[i] == x && tailY[i] == y)
            gameover = true;
    }

    if (x == fruitX && y == fruitY) 
    {
        score += 10;
        fruitX = rand() % width;
        fruitY = rand() % height;
        nTail++;
    }
}

int main() 
{
    //Initialize the game state
    Setup();
    

    while (!gameover) 
    {
        //Render Game Screen
        Draw();

        //Get User Input
        Input();

        //Update game logic
        Logic();

        //Game speed controller
        Sleep(100);
    }
    return 0;
}
