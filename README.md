VisionMeasure AI is a real-time computer vision system that detects, measures, and classifies physical objects using a standard A4 sheet as a reference. The project uses OpenCV for contour detection, perspective correction, and size calculation, along with MobileNetV2 for lightweight AI object classification.

## 🚀 Features
- 📏 **Real-time object measurement** using A4 paper as a reference
- 🎯 **Multi-object detection** with unique IDs
- 🤖 **AI classification** using MobileNetV2 (Caffe model)
- 🔍 Accurate width & height estimation in centimeters
- 📸 Supports **Camo Studio**, USB webcams, and laptop webcams
- 🔄 Automatic perspective correction
- 🧠 Lightweight + fast inference suitable for real-time processing

## 🛠 Technologies Used
- **Python**
- **OpenCV**
- **NumPy**
- **MobileNetV2 (Deep Learning Model)**

## 📚 How It Works
1. The system detects an **A4 sheet** using contour detection.  
2. It performs a **perspective warp** to convert the sheet into a top-down view.  
3. Objects placed on the sheet are detected and extracted.  
4. Each object's **dimensions are calculated** based on A4 scaling.  
5. The object is passed through **MobileNetV2** for classification.  
