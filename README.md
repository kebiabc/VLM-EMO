![image](https://github.com/kebiabc/VLM-EMO/assets/33951067/2d516ff0-ae07-4a48-bee8-a239d817a5ad)# VLM-EMO
This repo contains the official code of VLM-EMO Context-Aware Emotion Classification in the Wild with CLIP (VLM-EMO).
![VLM-EMO](https://github.com/kebiabc/VLM-EMO/assets/33951067/e9a05f99-954e-4df1-8e13-0c91c428af9d)

In the visual component, we leverage the CLIP image encoder as a foundation and introduce a temporal model, comprised of multiple Transformer Encoders, for capturing temporal features. 
The ultimate video-level facial features are generated via a trainable class token.

In the textual portion, we employ descriptions that pertain to behavior in lieu of class names as inputs for the text encoder. 
Additionally, we incorporate a trainable prompt to serve as contextual information for each class's descriptors.

# Rusults
![image](https://github.com/kebiabc/VLM-EMO/assets/33951067/7f18855c-a416-43d3-8b68-cd6623750d73)

![CAER-2401261508-cn](https://github.com/kebiabc/VLM-EMO/assets/33951067/93944755-5645-4db0-a770-09de915f71e2)

![image](https://github.com/kebiabc/VLM-EMO/assets/33951067/164314d0-6bc4-4e0f-aa7a-c26844d9fadc)


