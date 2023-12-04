// dllmain.cpp : 定义 DLL 应用程序的入口点。
#include "pch.h"
#include "vtkSmartPointer.h"
#include "vtkImageViewer2.h"
#include "vtkImageCast.h"
#include "vtkDICOMImageReader.h"
#include "vtkRenderWindow.h"
#include "vtkRenderWindowInteractor.h"
#include "vtkRenderer.h"
#include "vtkImageData.h"
#include "vtkCoordinate.h"


using namespace std;

BOOL APIENTRY DllMain( HMODULE hModule,
                       DWORD  ul_reason_for_call,
                       LPVOID lpReserved
                     )
{
    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}

extern "C" _declspec(dllexport) void readAndShowDICOM(const char* inputFilename,int* dims, unsigned char* data)
{
    vtkSmartPointer<vtkDICOMImageReader> reader =
        vtkSmartPointer<vtkDICOMImageReader>::New();

    // 读取DICOM图像
    vtkSmartPointer<vtkImageCast> imageCast =
        vtkSmartPointer<vtkImageCast>::New();

    reader->SetFileName(inputFilename);
    reader->Update();

    imageCast->SetInputConnection(reader->GetOutputPort());
    imageCast->SetOutputScalarTypeToInt();
    imageCast->Update();

    vtkImageData* imageData = imageCast->GetOutput();
    //int dims[3];
    
    imageData->GetDimensions(dims);
    // 复制图像数据
    int id = 0;
    for (int y = 0; y < dims[1]; y++) {
        for (int x = 0; x < dims[0]; x++) {
            unsigned char* pixel = static_cast<unsigned char*>(imageData->GetScalarPointer(x, y, 0));
            data[id] = pixel[0];
            id++;
        }
    }
}