#include <iostream>
#include <opencv2/opencv.hpp>
#include "dcmtk/dcmdata/dctk.h"
#include "dcmtk/dcmimgle/dcmimage.h"

cv::Mat read_dicom_image(const std::string& file_path) {
    DcmFileFormat file_format;
    OFCondition status = file_format.loadFile(file_path.c_str(), EXS_Unknown);
    if (status.bad()) {
        std::cerr << "Error loading DICOM file: " << status.text() << std::endl;
        return cv::Mat();
    }

    DcmDataset* dataset = file_format.getDataset();
    if (!dataset) {
        std::cerr << "Error accessing DICOM dataset" << std::endl;
        return cv::Mat();
    }

    OFString photometric_interpretation;
    status = dataset->findAndGetOFString(DCM_PhotometricInterpretation, photometric_interpretation);
    if (status.bad()) {
        std::cerr << "Error getting PhotometricInterpretation: " << status.text() << std::endl;
        return cv::Mat();
    }

    DicomImage* dicom_image = new DicomImage(file_path.c_str(), EXS_Unknown);
    if (dicom_image->getStatus() != EIS_Normal) {
        std::cerr << "Error loading DICOM image: " << DicomImage::getString(dicom_image->getStatus()) << std::endl;
        delete dicom_image;
        return cv::Mat();
    }

    unsigned int width = dicom_image->getWidth();
    unsigned int height = dicom_image->getHeight();
    unsigned char* pixel_data = (unsigned char*)(dicom_image->getOutputData(8));

    cv::Mat image(height, width, CV_8UC1, pixel_data);

    if (photometric_interpretation == "MONOCHROME1")
        cv::bitwise_not(image, image);

    delete dicom_image;
    return image;
}

int main() {
    std::string file_path = "<DICOMÎÄ¼þÂ·¾¶>";

    cv::Mat image = read_dicom_image(file_path);

    if (image.empty()) {
        std::cerr << "Failed to read DICOM image!" << std::endl;
        return 1;
    }

    cv::namedWindow("DICOM Image");
    cv::imshow("DICOM Image", image);
    cv::waitKey(0);
    cv::destroyAllWindows();

    return 0;
}