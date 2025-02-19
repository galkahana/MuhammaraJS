{
    'targets': [
        {
           'target_name': 'zlib',
           'type': 'static_library',
           'msvs_settings':
			{
				'VCCLCompilerTool':
				{
					'AdditionalOptions':
						[
						'/std:c++20',
						]
				}
			},
            'sources': [
                'adler32.c',
                'compress.c',
                'crc32.c',
                'deflate.c',
				'gzclose.c',
				'gzlib.c',
				'gzread.c',
				'gzwrite.c',
                'infback.c',
                'inffast.c',
                'inflate.c',
                'inftrees.c',                
                'trees.c',
                'uncompr.c',
                'zutil.c',
                'crc32.h',
                'deflate.h',
                'gzguts.h',
                'inffast.h',
                'inffixed.h',
                'inflate.h',
                'inftrees.h',
                'trees.h',
                'zconf.h',
                'zlib.h',
                'zutil.h'
            ]
        }
    ]        
}
