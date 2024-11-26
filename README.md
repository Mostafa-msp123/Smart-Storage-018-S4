# Smart-Storage-018-S4
### Capstone Project: **Smart Storage**

### **Summary**

#### **Problem**  
Determining the number of products entering the warehouse daily,
as it is difficult for warehouse workers to determine the number of products entering the warehouse 
daily for many reasons, including the large number of products entering the warehouse or the presence
of errors in the system. There are products entering the warehouse that are merged products, and the
product inside them is spoiled because this product is for merger.


#### **Solution**  
We will train the camera on the products in the warehouse and the damaged products within,
the warehouse so that if there is a merged product carton, the camera will recognize it and,
remove it from the conveyor belt. It will also determine the validity of the product and ,
categorize it into two types. The camera will send a CSV file with the product count and ,
the validity of each item. Additionally, we can add a feature where if someone takes a product,
an immediate message will be sent to the warehouse manager with the number of products that have ,
been withdrawn. Furthermore, if a product passes through the conveyor belt and is not detected,
the conveyor belt will stop for five minutes, and the red LED light and buzzer will activate. 
Once the product is correctly detected, the product will be registered, and the green LED light will turn on

#### **Problem Statement**
Warehouse workers struggle to accurately track daily incoming products due to:  
- High product volume.  
- System errors.  
- Presence of merged cartons containing defective items.

#### **Proposed Solution**
1. **Camera-Based Monitoring:**
   - Identify standard and merged product cartons.  
   - Remove defective cartons from the conveyor belt.

2. **Product Validation & Reporting:**
   - Validate product condition and categorize as valid or defective.  
   - Generate a **CSV file** with product count and validity status.

3. **Real-Time Alerts:**
   - Notify the warehouse manager of product withdrawals with counts.

4. **Error Handling:**
   - Stop the conveyor belt for 5 minutes if a product passes undetected.  
   - Activate red LED and buzzer, resuming only after proper detection.  

#### **Key Features**
- **Automated Tracking:** Real-time product counting and defect detection.  
- **Error Mitigation:** Prevents defective products from being stored.  
- **Notifications:** Alerts for product withdrawals.  
- **Safety Mechanisms:** Stops operations for undetected items.  

#### **Next Steps**
- Develop and train the detection model.  
- Integrate hardware with software modules.  
- Perform testing in a warehouse environment.  
- Deploy and optimize based on user feedback.  
