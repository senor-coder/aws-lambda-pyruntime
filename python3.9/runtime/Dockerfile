FROM lambci/lambda-base

ARG RUNTIME_PACKAGE_URL

RUN curl "$RUNTIME_PACKAGE_URL" | tar -zx -C /opt

FROM lambci/lambda:provided

FROM lambci/lambda-base-2

ENV PATH=/var/lang/bin:$PATH \
    LD_LIBRARY_PATH=/var/lang/lib:$LD_LIBRARY_PATH \
    AWS_EXECUTION_ENV=AWS_Lambda_python3.9

COPY --from=0 /opt/* /var/

COPY --from=1 /var/runtime/init /var/rapid/init

USER sbx_user1051

ENTRYPOINT ["/var/rapid/init", "--bootstrap", "/var/runtime/bootstrap", "--enable-msg-logs"]