{
  'lcm-log': 'lcm-logs/moving-camera.lcmlog',
  'camera-poses': 'efusion-output/moving-camera/moving-camera.lcmlog.posegraph',
  'reconstruction': 'efusion-output/moving-camera/moving-camera.lcmlog.vtp',
  'object-registration': [
    {
      'name': 'phone',
      'filename': 'object-meshes/phone.vtp',
      'pose': [[0.7606531401738793, -0.03765840618820415, -0.25154909742658227],
               [-0.3792756487669554, -0.39252408872388406, -0.16826477945296256, 0.8208299373314398]]
    },
    {
        'name': 'robot',
        'filename': 'object-meshes/robot.vtp',
        'pose': [[0.7842449543284591, 0.11163584822030512, -0.18685480815812347],
                 [0.2309385207829862, 0.05044505545914463, 0.609926128290588, 0.7563813945535318]]
    },
    {
        'name': 'toothpaste',
        'filename': 'object-meshes/toothpaste.vtp',
        'pose': [[0.6929176068341711, -0.12187048508851923, -0.20570028909384638],
                 [0.5372201635849231, -0.5409129925293267, -0.5571220340038646, 0.3292759778334113]]
    },
    {
        'name': 'oil_bottle',
        'filename': 'object-meshes/mobil1_v1.vtp',
        'pose': [[0.8339119515772663, -0.0007036806779457492, -0.13099183653456142],
                 [0.3793151463799564, 0.62242821819055, -0.4941473187958157, -0.4738370608698672]]
    }]
}
