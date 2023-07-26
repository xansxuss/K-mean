#include <iostream>
#include <vector>
#include <dirent.h>
#include <typeinfo>
#include <string.h>

// #include <array.h>
#include "opencv2/core.hpp"
#include "opencv2/imgproc.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/videoio.hpp"

using std::cin;
using std::cout;
using std::endl;
using std::vector;
using namespace cv;
using namespace std;

void getfilename(string path,              // path type str
                 vector<string> &filenames // defind str container
)
{
    DIR *pDir;
    struct dirent *ptr;
    if (!(pDir = opendir(path.c_str())))
        return;
    while ((ptr = readdir(pDir)) != 0)
    {
        if (strcmp(ptr->d_name, ".") != 0 && strcmp(ptr->d_name, "..") != 0)
            filenames.push_back(path + "/" + ptr->d_name);
    }
    closedir(pDir);
}

int main()
{
    Mat image;
    Mat out_img, img_2;
    // vector<string> file_name;
    // string path = "/home/xanxus/Desktop/368_data/img_out/data/data_0/tt";

    // getfilename(path, file_name);
    // for (int i = 0; i < file_name.size(); i++)
    // {
    //     cout << file_name[i] << endl;

    //     image = imread(file_name[i], 1);

    //     cout << "size:" << image.size() << endl;
    //     cout << "elemsize:" << image.elemSize() << endl;
    //     cout << "channels:" << image.channels() << endl;
    //     cout << "depth:" << image.depth() << endl;
    //     namedWindow("display", WINDOW_AUTOSIZE);
    //     imshow("display", image);
    //     waitKey(1000);
    // }

    out_img = imread("/home/xanxus/Desktop/368_data/img_out/data/data_0/tt/0_0_out_0.jpg", 1);
    resize(out_img, img_2, Size(32, 32), 0, 0, INTER_LINEAR);
    cout << img_2 << endl;
    // {
    //     string pname;
    //     cout << path << "/" << file;
    //     pname.append(path).append("/").append(file);

    //     Mat image;
    //     image = imread(pname, 10);
    //     namedWindow("display", WINDOW_AUTOSIZE);
    //     imshow("display", image);
    //     waitKey(0);
    //     continue;
    // }

    // int length;
    // int s[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    // int *p = s;
    // cout << sizeof(s) << endl;
    // cout << sizeof(s) << endl;
    // cout << s << endl;
    // cout << p << endl;
    // length = sizeof(s) / sizeof(s[0]);
    // // arr(s, length);

    // for (int i = 0; i < length; i++)
    // {
    //     cout << "s[" << i << "]=" << s[i] << '\n';

    //     cout << "*p[" << i << "]=" << *(p + 1) << '\n';
    //     cout << "p[" << i << "]=" << p[i] << '\n';
    //     cout << "p[" << i << "]=" << &p[i] << '\n';
    //     // }

    // Mat image;
    // image = imread("../cat.jpg", 1);
    // namedWindow("display", WINDOW_AUTOSIZE);
    // imshow("display", image);
    // waitKey(0);
    return 0;
}