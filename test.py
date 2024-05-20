from PIL import Image
import numpy as np


def blend_images(image_path1, image_path2, p1, p2, output_path):
    # 打开图片
    image1 = Image.open(image_path1)
    image2 = Image.open(image_path2)

    # 确保两张图片的尺寸相同
    if image1.size != image2.size:
        raise ValueError("两张图片的尺寸必须相同")

    # 将图片转换为numpy数组
    array1 = np.array(image1)
    array2 = np.array(image2)

    # 计算加权和
    blended_array = p1 * array1 + p2 * array2

    # 确保像素值在0到255之间
    blended_array = np.clip(blended_array, 0, 255).astype(np.uint8)

    # 将numpy数组转换为图片
    blended_image = Image.fromarray(blended_array)

    # 保存合成后的图片
    blended_image.save(output_path)


# 使用示例
image_path1 = "/Users/happyelements/Downloads/1.png"
image_path2 = "/Users/happyelements/Downloads/3.png"
weight = 0.01
# p1是weight的平方根
p1 = weight**0.5
p2 = 1 - p1
output_path = "/Users/happyelements/Downloads/rrr1.png"

blend_images(image_path1, image_path2, p1, p2, output_path)
