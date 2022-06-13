import pygame
from screen import screen1

pygame.init()

class Text:
    def __init__(self, text_chars, x, y, font_size, align="", color = (255,255,255)):
        self.text_chars = text_chars
        self.font_size = font_size
        self.font_color = color
        self.font = self.configure_font()
        self.font_rendered = self.font_render()
        self.rect = self.font_rendered.get_rect()
        self.area = [self.rect[2], self.rect[3]]
        self.align = align
        self.x = x
        self.y = y
        self.centerx, self.centery = [0,0]
        self.set_center()
        if self.align == "center":
            self.set_alignment()

        self.textAlignLeft = 0
        self.textAlignRight = 1
        self.textAlignCenter = 2
        self.textAlignBlock = 3

    def configure_font(self):
        return pygame.font.SysFont("verdana", self.font_size)

    def font_render(self):
        return self.font.render(self.text_chars, True, self.font_color)

    def draw(self):
        screen1.blit(self.font_rendered, (self.x, self.y))

    def set_center(self):
        self.centerx, self.centery = self.x - self.area[0] / 2, self.y - self.area[1] / 2

    def set_alignment(self):
        self.x = self.centerx
        self.y = self.centery

    def move(self, x, y):
        self.x = x
        self.y = y
        self.set_center()
        if self.align == "center":
            self.set_alignment()

    def drawParagraph(self, rect, align=0, aa=True, bkg=None):
        lineSpacing = -2
        spaceWidth, fontHeight = self.font.size(" ")[0], self.font.size("Tg")[1]

        listOfWords = self.text_chars.split(" ")
        if bkg:
            imageList = [self.font.render(word, True, self.font_color, bkg) for word in listOfWords]
            for image in imageList: image.set_colorkey(bkg)
        else:
            imageList = [self.font.render(word, aa, self.font_color) for word in listOfWords]

        maxLen = rect[2]
        lineLenList = [0]
        lineList = [[]]
        for image in imageList:
            width = image.get_width()
            lineLen = lineLenList[-1] + len(lineList[-1]) * spaceWidth + width
            if len(lineList[-1]) == 0 or lineLen <= maxLen:
                lineLenList[-1] += width
                lineList[-1].append(image)
            else:
                lineLenList.append(width)
                lineList.append([image])

        lineBottom = rect[1]
        lastLine = 0
        for lineLen, lineImages in zip(lineLenList, lineList):
            lineLeft = rect[0]
            if align == self.textAlignRight:
                lineLeft += + rect[2] - lineLen - spaceWidth * (len(lineImages) - 1)
            elif align == self.textAlignCenter:
                lineLeft += (rect[2] - lineLen - spaceWidth * (len(lineImages) - 1)) // 2
            elif align == self.textAlignBlock and len(lineImages) > 1:
                spaceWidth = (rect[2] - lineLen) // (len(lineImages) - 1)
            if lineBottom + fontHeight > rect[1] + rect[3]:
                break
            lastLine += 1
            for i, image in enumerate(lineImages):
                x, y = lineLeft + i * spaceWidth, lineBottom
                screen1.blit(image, (round(x), y))
                lineLeft += image.get_width()
            lineBottom += fontHeight + lineSpacing

        if lastLine < len(lineList):
            drawWords = sum([len(lineList[i]) for i in range(lastLine)])
            remainingText = ""
            for text in listOfWords[drawWords:]: remainingText += text + " "
            return remainingText
        return ""





