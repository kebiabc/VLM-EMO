# VLM-EMO
This repo contains the official code of VLM-EMO Context-Aware Emotion Classification in the Wild with CLIP (VLM-EMO).
![VLM-EMO](https://github.com/kebiabc/VLM-EMO/assets/33951067/e9a05f99-954e-4df1-8e13-0c91c428af9d)
In the visual component, we leverage the CLIP image encoder as a foundation and introduce a temporal model, comprised of multiple Transformer Encoders, for capturing temporal features. The ultimate video-level facial features are generated via a trainable class token.
In the textual portion, we employ descriptions that pertain to behavior in lieu of class names as inputs for the text encoder. Additionally, we incorporate a trainable prompt to serve as contextual information for each class's descriptors.

# Rusults
![image](https://github.com/kebiabc/VLM-EMO/assets/33951067/62c9f4a4-2b84-4c14-aaed-465facb24906)
![CAER-2310112146-cn](https://github.com/kebiabc/VLM-EMO/assets/33951067/3188a9ca-1a30-4abf-bfae-963cd9747914)
