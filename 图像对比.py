import cv2


# 自定义计算两个图片相似度函数
def img_similarity(img1_path, img2_path):
    """
    :param img1_path: 图片1路径
    :param img2_path: 图片2路径
    :return: 图片相似度
    """
    try:
        # 读取图片
        img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)
        
        # 初始化ORB检测器
        orb = cv2.ORB_create()
        kp1, des1 = orb.detectAndCompute(img1, None)
        kp2, des2 = orb.detectAndCompute(img2, None)
        
        # 提取并计算特征点
        bf = cv2.BFMatcher(cv2.NORM_HAMMING)
        
        # knn筛选结果
        matches = bf.knnMatch(des1, trainDescriptors=des2, k=2)
        
        # 查看最大匹配点数目
        good = [m for (m, n) in matches if m.distance < 0.75 * n.distance]
        print(len(good))
        print(len(matches))
        similary = len(good) / len(matches)
        print("两张图片相似度为:%s" % similary)
        return similary
    
    except:
        print('无法计算两张图片相似度')
        return '0'


if __name__ == '__main__':
    img1_path = '7ba.jpg'
    img2_path = 'ba.jpg'
    similary = img_similarity(img1_path, img2_path)
