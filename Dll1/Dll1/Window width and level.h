#pragma once
#ifndef WINDOW_WIDTH_AND_LEVEL_H
#define WINDOW_WIDTH_AND_LEVEL_H

#include <string>

#ifdef __cplusplus
extern "C" {
#endif

#ifdef _MSC_VER
#ifdef WINDOW_WIDTH_AND_LEVEL_DLL
#define WINDOW_WIDTH_AND_LEVEL_API __declspec(dllexport)
#else
#define WINDOW_WIDTH_AND_LEVEL_API __declspec(dllimport)
#endif
#else
#ifdef WINDOW_WIDTH_AND_LEVEL_DLL
#define WINDOW_WIDTH_AND_LEVEL_API __attribute__((visibility("default")))
#else
#define WINDOW_WIDTH_AND_LEVEL_API
#endif
#endif

#include <opencv2/core.hpp>

    WINDOW_WIDTH_AND_LEVEL_API void displayDICOMImage(const std::string& filePath, int windowWidth, int windowCenter);

#ifdef __cplusplus
}
#endif

#endif