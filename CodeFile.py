#coding:utf-8

import os
import re
import random
import io


## 方法重命名

project_path = '/Users/chenying/Desktop/ufoto/facefoto/CSYCamera'
suf_set = ('.h', '.m', '.xib', '.mm', '.pch', '.swift')


func_name_pre = [
  "configurationRootViewController",
  "searchContact",
  "addToSession",
  "change2English",
  "resizeImage",
  "addAnimatiosn",
  "stringWidthFont",
  "createButton",
  "startPlaying",
  "stopPlaying",
  "audioRecorderUpdateMetra",
  "startRecord",
  "readyStartRecord",
  "stopRecord",
  "readyStopRecord",
  "updateMeters",
  "audioRecorderEncodeErrorDidOccur",
  "showMenuAction",
  "copyAction",
  "transtionAction",
  "deleteAction",
  "moreAciton",
  "hiddenMenuController",
  "tapTableView",
  "clickCellAction",
  "voiceClick",
  "recordClick",
  "recordComplection",
  "recordDragOut",
  "recordCancel",
  "emotionClick",
  "moreClick",
  "shareMoreClick",
  "beginVideoRecord",
  "videoBackgroundViewClick",
  "videoRecordComplection",
  "sendImage",
  "imagePickerController",
  "imagePickerControllerDidCancel",
  "mapViewController",
  "imagePickerControllerCanceled",
  "selectEmoji",
  "textView",
  "addNotificationToDevice",
  "removeNotificationFromDevice",
  "removeNotification",
  "notificateAreChanged",
  "sessionWasInterrupted",
  "sessionInterruptEnd",
  "notificateSessionError",
  "beginRecord",
  "complectionRecord",
  "cancelRecord",
  "changeCameraPosition",
  "setFlashMode",
  "setFocusMode",
  "setFocusExposureMode",
  "captureOutput",
  "tapView",
  "removeConfigure",
  "setPlayUrl",
  "setPlayAsset",
  "configurationItem",
  "observeValueForKeyPath",
  "videoPlayDidEnd",
  "converTimer",
  "configureSlider",
  "monitoringPlayback",
  "layerClass",
  "customInit",
  "buttonTouchDown",
  "buttonDragOutside",
  "buttonCancel",
  "buttonTouchUp",
  "stopTimers",
  "recordTimerUpdate",
  "preView",
  "animationControllerForDismissedController",
  "animationControllerForPresentedController",
  "selectButton",
  "updateAssetChache",
  "assetAtIndexPath",
  "indexPathInRect",
  "transitionDuration",
  "animateTransition",
  "stopPlayer",
  "playLivePhoto",
  "getTargetSize",
  "updateImage",
  "updateLivePhoto",
  "updateStaticImage",
  "setupCollectionView",
  "setupNavgationBar",
  "selectCurrentImage",
  "dismissView",
  "setSelect",
  "getCollectionList",
  "locationManager",
  "mapView",
  "startSearch",
  "emojiClick",
  "setupEmotionWith",
  "setMessage",
  "setSelected",
  "updateLevelMetra",
  "showMetraLevel",
  "showIndicatorImage",
  "showRecord",
  "showEmotion",
  "showMore",
  "canPerformAction",
  "stopAnimation",
  "beginAnimation",
  "setUpVoicePlayIndicatorImageView",
  "setupCamera",
  "setupScanLine",
  "makeScanReaderRect",
  "makeScanReaderInterestRect",
  "makeScanCameraShadowView",
  "scanLineAnimation",
  "showScanCode",
  "showAlterView",
  "updateCell",
  "didSelectedLeftButton",
  "didSelectedRightButton",
  "removeOldTableViewPanObserver",
  "setLeftButtons",
  "setRightButtons",
  "selectCell",
  "deselectCell",
  "rightButtonHandler",
  "leftButtonHandle",
  "hiddenButtonsAnimated",
  "showLeftButtonsAnimated",
  "showRightButtonsAnimated",
  "hiddenOtherCells",
  "isButtonsHidden",
  "leftButtonsWidth",
  "rightButtonsWidth",
  "totalButtonsWidth",
  "contentOffsetForCellStatus",
  "updateCellStatus",
  "setupButton",
  "pushBackgroundColor",
  "popBackgroundColor",
  "defaultExpectation",
  "testLogCollectorDoesNotCollectPreviousLogs",
  "testLogCollectorHasNoLogsInitially",
  "setUpScreenshotButton",
  "screenshotButtonTapped",
  "setSecondControlPoint",
  "scaledPoint",
  "motionEnded",
  "retrieveLogs",
  "arrowBezierPath",
  "setTitleTextAttributesForAllStates",
  "failRecognizing",
  "keyboardWillChangeFrame",
  "updateAndStore",
  "firstOrSecondItem",
  "shakeDetectingWindowDidDetectShake",
  "updateDataSource",
  "updateInterfaceCustomization",
  "sendButtonTapped",
  "cancelButtonTapped",
  "collectFeedback",
  "editorWillDismiss",
  "feedbackTableViewDataSource",
  "commonInitialization",
  "presentFailureToComposeMailAlert",
  "feedbackCollector",
  "pinpointKit",
  "setUpTextView",
  "viewLog",
  "pinpointTopModalViewController",
  "updateTextViewFrame",
  "beginEditing",
  "pinpointKitBundle",
  "glkView",
  "succeed",
  "mailComposeController",
  "completeWithResult",
  "bringSubviewToFront",
  "moveViewIfAppropriate",
  "moveBlurViewAboveBlurViewsAndUnderOthers",
  "sourceSansProFont",
  "menloRegularFont",
  "sectionsFromConfiguration",
  "checkmarkCell",
  "screenshotCell",
  "numberOfSections",
  "takeScreenshot",
  "drawGlyphs",
  "showCGGlyphs",
  "pinpointOrange",
  "loadImage",
  "annotationView",
  "attemptToDismiss",
  "setupConstraints",
  "doneButtonTapped",
  "handleTouchDownGestureRecognizer",
  "imageIsLandscape",
  "beginEditingTextView",
  "forceEndEditingTextView",
  "endEditingTextViewIfFirstResponder",
  "endEditingTextView",
  "handleGestureRecognizerFinished",
  "toolChanged",
  "handleCreateAnnotationGestureRecognizer",
  "handleCreateAnnotationGestureRecognizerBegan",
  "handleCreateAnnotationGestureRecognizerChanged",
  "handleUpdateAnnotationGestureRecognizer",
  "handleUpdateAnnotationGestureRecognizerBegan",
  "handleUpdateAnnotationGestureRecognizerChanged",
  "handleUpdateAnnotationTapGestureRecognizer",
  "handleUpdateAnnotationPinchGestureRecognizer",
  "handleUpdateAnnotationPinchGestureRecognizerBegan",
  "handleUpdateAnnotationPinchGestureRecognizerChanged",
  "handleDoubleTapGestureRecognizer",
  "handleLongPressGestureRecognizer",
  "deleteAnnotationView",
  "deleteSelectedAnnotationView",
  "informDelegate",
  "clearAllAnnotations",
  "editorShouldDismiss",
  "editorDidDismiss",
  "userTookScreenshot",
  "requestPhotosAuthorization",
  "findScreenshot",
  "screenshotDetector",
  "fetchLastScreenshot",
  "highQualitySynchronousLocalOptions",
  "photoLibraryDidChange",
  'pixelFrameLoopE', 'customRenderD', 'customRenderO', 'customVerticesA', 'linkIndexB', 'frameLoopS', 'checkAllLiveD', 'calcFPSF', 'unlistenToFramesS', 'unfollowTimeF', 'loadMetalShaderLibraryC', 'makeQuadVertecisG', 'makeQuadVertexBufferS', 'loadQuadVertexShaderC', 'makeVertexShaderF', 'makeTextureCacheE', 'makeFragS', 'makeMetalFragE', 'makeMetalFragG', 'makeShaderPipelineO', 'makeSamplerI', 'rawNormalizedG', 'embedMetalCodeS', 'dynamicUniformsS', 'zfillOrgO', 'updateSamplerD', 'setNeedsRenderF', 'didRenderE', 'renderOutsG', 'renderCustomVertexTextureA', 'setNeedsConnectB', 'disconnectedD', 'connectMultiA', 'customLinkS', 'customDelinkA', 'checkLiveE', 'destroyF', 'pixResChangedB', 'pixDidRenderO', 'operatorNameB', 'aspectResS', 'aspectBoundsS', 'reFrameF', 'anchorXF', 'anchorXE', 'anchorYS', 'anchorYS', 'anchorXD', 'anchorYI', 'anchorXD', 'anchorXA', 'anchorXS', 'anchorYI', 'anchorYB', 'anchorYF', 'removeResE', 'autoLiveBoolsG', 'autoLiveColorsD', 'autoLiveFloatsI', 'autoLiveIntsE', 'autoLivePointsI', 'autoLiveRectsF', 'autoLiveSizesF', 'autoEnumsB', 'autoLiveBoolsO', 'autoLiveColorsC', 'autoLiveFloatsG', 'autoLiveIntsF', 'autoLivePointsS', 'autoLiveRectsO', 'autoLiveSizesF', 'autoEnumsC', 'autoLiveBoolsD', 'autoLiveColorsA', 'autoLiveFloatsA', 'autoLiveIntsG', 'autoLivePointsG', 'autoLiveRectsA', 'autoLiveSizesG', 'autoEnumsB', 'autoLiveBoolsG', 'autoLiveColorsB', 'autoLiveFloatsO', 'autoLiveIntsB', 'autoLivePointsO', 'autoLiveRectsI', 'autoLiveSizesB', 'autoEnumsB', 'startRecD', 'pauseRecS', 'resumeRecC', 'realtimeListenS', 'frameLoopI', 'didRenderB', 'startRecordG', 'pauseRecordG', 'resumeRecordI', 'setupAudioG', 'recordFrameE', 'appendPixelBufferForImageAtURLO', 'captureOutputA', 'destroyB', 'setNeedsRenderI', 'destroyF', 'addAirPlayViewC', 'connectAirPlayA', 'disconnectAirPlayI', 'screenConnectS', 'screenDisconnectF', 'appActiveC', 'disconnectC', 'didRenderI', 'connectE', 'disconnectB', 'reFrameO', 'anchorXB', 'anchorXB', 'anchorYS', 'anchorYC', 'anchorXI', 'anchorYS', 'rainbowA', '_gradientMapO', 'reFrameD', 'anchorXO', 'anchorXI', 'anchorYD', 'anchorYD', 'anchorXD', 'anchorYB', 'reFrameD', 'anchorXS', 'anchorXB', 'anchorYC', 'anchorYB', 'anchorXG', 'anchorYD', 'bakeFragA', 'makePipelineO', 'reFrameS', 'anchorXD', 'anchorXA', 'anchorYD', 'anchorYG', 'anchorXA', 'anchorYB', 'reFrameG', 'anchorXD', 'anchorXF', 'anchorYO', 'anchorYF', 'anchorXD', 'anchorYS', 'setNeedsRenderE', 'setNeedsTextI', 'setNeedsTextColorC', 'setNeedsFontO', 'setNeedsPositionB', 'setNeedsBufferI', 'setupScreenCaptureB', 'captureOutputG', 'glSetupB', 'seekSecondsO', 'seekFractionI', 'setRateD', 'restartB', 'thumbnailF', 'thumbnailC', 'readBufferS', 'observeValueE', 'getOrientationO', 'playerItemDidReachEndB', 'setNeedsBufferA', 'setNeedsBufferS', 'cameraSetupC', 'cameraFrameG', 'setupCameraD', 'camAttatchedE', 'camDeattatchedI', 'deviceRotatedF', 'captureOutputC', 'depthDataOutputD', 'manualExposureB', 'manualFocusB', 'manualWhiteBalanceS', 'setLightO', 'setTorchS', 'setFocusC', 'setWhiteBalanceC', 'getExposureO', 'getFocusPointF', 'getWhiteBalanceS', 'captureC', 'photoOutputC', 'makeUniqueTempFileURLS', 'destroyB', 'buildGridG', 'buildHexagonalGridC', 'buildCircleF', 'buildLineC', 'buildRandomB', 'cacheTextureE', 'customRenderS', '_quantizeC', 'customVerticesC', 'cornerPinB', 'mapVerticesC', '_brightnessO', '_darknessG', '_contrastB', '_invertB', '_opacityA', '_sharpenO', '_flopLeftF', '_flopRightA', 'setNeedsRenderS', 'customRenderB', 'guassianBlurS', '_zoomBlurA', 'didRenderC', 'resetFeedO', '_kaleidoscopeD', 'destroyB', 'customRenderF', '_chromaKeyO', 'setNeedsRenderO', '_freezeA', '_cropLeftA', '_cropRightD', '_cropTopO', '_cropBottomA', '_thresholdD', '_saturationF', '_monochromeD', '_lumaToAlphaB', '_rotatateE', '_rotatateD', '_rotatateE', '_lumaBlurE', '_tiltShiftI', '_lumaLevelsD', '_vignettingF', '_lookupC', '_reorderI', '_replaceO', '_RGtoBAA', '_displaceB', '_noiseDisplaceG', 'frameLoopE', 'customRenderG', 'customRenderI', 'reFrameD', 'anchorXF', 'anchorXE', 'anchorYB', 'anchorYS', 'anchorXA', 'anchorYB', 'frameSizeD', 'resScaleB', 'destroyG', 'gotMidiC', 'listenToDeviceS', 'unlistenToDeviceC', 'getSourceNamesC', 'getDisplayNameC', 'startHostingO', 'joinSessionF', 'sendImgA', 'sendCheckedI', 'sendDisconnectD', 'sessionD', 'sessionI', 'ioCheckE', 'sessionC', 'sessionG', 'sessionO', 'browserViewControllerDidFinishF', 'browserViewControllerWasCancelledS', 'updateTrackingAreasI', 'mouseMovedE', 'mouseDraggedI', 'rightMouseDraggedO', 'mouseDownC', 'mouseUpS', 'rightMouseDownB', 'rightMouseUpF', 'mouseEnteredA', 'mouseExitedD', 'getCoordF', 'autoLayoutE', 'layoutPlacementA', 'liveTouchC', 'liveMouseO', 'touchesBeganF', 'touchesMovedD', 'touchesEndedC', 'touchesCancelledE', 'checkerImageC', 'liveRandomI', 'liveRandomD', 'truncatingRemainderA', 'remainderC', 'liveRandomI', 'liveRandomO', 'relativeG', 'maximumS', 'minimumG', 'withAlphaE', 'withHueD', 'withSatF', 'withValI', 'withShiftedHueA', 'liveCircleG', 'topLeftB', 'topRightC', 'bottomLeftE', 'bottomRightF', 'pointFromA', 'formatCleanG', 'logLengthA', 'renderPIXsD', 'makeTextureS', 'makeTextureS', 'emptyTextureI', 'copyTextureD', 'makeMultiTextureE'

]

def file_classname_in_path(file_path):
    print(file_path)
    
    fileClassName = ''
    with open(file_path, 'rb+') as f:
#    with io.open(file_path, 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
        
            if line.strip().startswith('return'):
                continue
            
            if line.__contains__('extension'.encode()):
                
                if line.strip().startswith('//'):
                    continue
                
                if line.strip().startswith('protocol'):
                    continue
                    
                print(line.split())
                index = 0

                classItems = line.split()
                for classitem in classItems:
                    index +=1
                    if classitem.__contains__('extension'.encode()):
#                        print('iiiiiiiii:' + str(index) + 'classitem:' + classitem)
                        break
                
                realClass = classItems[index]
                fileClassName = realClass.replace("{", " ").replace("(", " ").replace(":", " ")
                print('realClass:' + fileClassName)
                break

            elif line.__contains__('class'.encode()):
                if line.strip().startswith('//'):
                    continue
                
                if line.strip().startswith('protocol'):
                    continue
                
                if line.strip().startswith('@class'):
                    continue
                
                if line.strip().startswith('#import'):
                    continue
                
                if line.strip().endswith(';'):
                    continue
                
                print(line.split())
                index = 0

                classItems = line.split()
                for classitem in classItems:
                    index +=1
                    if classitem.__contains__('class'.encode()):
                #                                print('iiiiiiiii:' + str(index) + 'classitem:' + classitem)
                        break
                                
                realClass = classItems[index]
                fileClassName = realClass.replace("{", " ").replace("(", " ").replace(":", " ")
                print('realClass:' + fileClassName)
                break
                
                
            elif line.__contains__('@implementation'.encode()):
                if line.strip().startswith('//'):
                    continue
                
                if line.strip().startswith('@protocol'):
                    continue
                
                if line.strip().__contains__('('.encode()):
                    continue
                
                print(line.split())
                index = 0

                classItems = line.split()
                for classitem in classItems:
                    index +=1
                    if classitem.__contains__('@implementation'.encode()):
                #                                print('iiiiiiiii:' + str(index) + 'classitem:' + classitem)
                        break
                                
                realClass = classItems[index]
                fileClassName = realClass.replace("{", " ").replace("(", " ").replace(":", " ")
                print('realClass:' + fileClassName)
                break
#
#            elif line.__contains__('@interface'.encode()):
    return fileClassName
    


def refactor_variable():
    for (root, dirs, files) in os.walk(project_path):
        for file_name in files:
            print(file_name)
            with open(os.path.join(root, file_name), 'rb+') as f:
                lines = f.readlines()
                for line in lines:
                    if line.__contains__('@property'.encode()):
                        str = line.decode()
                        print(line.decode())
                        result = re.findall(".*\*(.*);.*", line.decode())
                        if result.__len__() > 0:
                            v = re.findall(".*\*(.*);.*", line.decode())[0]
                            new_v = v + "_mjt"
                            str.replace(v,new_v)
                            print(new_v)

def fool_code():
    for (root, dirs, files) in os.walk(project_path):
        for file_name in files:
            print(file_name)
            if os.path.splitext(file_name)[1] == '.swift':
#                class_name = os.path.splitext(file_name)[0]
                class_name = file_classname_in_path(os.path.join(root, file_name))
                if len(class_name) < 2:
                    continue
                    
                with open(os.path.join(root, file_name), 'a') as f:
                    f.write('\nfileprivate extension ' + class_name + "{ " +  random_function_str() + "\n}" )
            elif os.path.splitext(file_name)[1] == '.m' or os.path.splitext(file_name)[1] == '.mm':
                if os.path.splitext(file_name)[0].count('+') > 0: #过滤自身就是扩展的文件
                    continue
                

#                if file_name.find("extension") != -1:
#                    continue
#                class_name = os.path.splitext(file_name)[0]
                class_name = file_classname_in_path(os.path.join(root, file_name))
                if len(class_name) < 2:
                    continue
                    
                with open(os.path.join(root, file_name), 'a') as f:
                    str =  "\n@interface {0}({1}) \n@end\n @implementation {0}({1}) {2} \n@end\n".format(class_name, radom_str(),random_function_str(is_swift=False))
                    print(str)
                    f.write(str)

def random_function_str(is_swift = True):
    # 随机数量方法
    func_count = random.randrange(2,14)
    func_names = []
    for i in range(func_count):
        name = radom_str()
        if not func_names.__contains__(name):
            func_names.append(name)

    func_str = ''
    for idx in range(len(func_names)):
        if is_swift:
            func_str += "\n    func " + func_names[idx] + "(){" + random_call_function_str(func_names, is_swift=is_swift) + "\n    }\n"
        else:
            func_str += "\n- (void){0} {{ {1} }} \n".format(func_names[idx], random_call_function_str(func_names, is_swift=is_swift))
            # print(random_call_function_str(func_names, is_swift=is_swift))
    # print(func_str)
    return func_str

def random_call_function_str(func_names,is_swift = True):
    func_count = random.randrange(1, len(func_names))
    call_func_names = []
    for i in range(func_count):
        name = radom_str()
        if not call_func_names.__contains__(name):
            call_func_names.append(random.choice(func_names))
    call_func_str = ''
    for func_name in call_func_names:
        # if random.randrange(0,2) == 1 and func_count > 1 :
        #     call_func_str += "\n"
        if is_swift:
            call_func_str += "\n      {0}()".format(func_name)
        else:
            call_func_str += "\n    [self {0}];\n".format(func_name)
    return call_func_str


def radom_str():
    return random.choice(func_name_pre)

# refactor_variable()
if __name__ == '__main__':
    fool_code()
